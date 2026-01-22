import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np
import os

# 1. 페이지 설정
st.set_page_config(page_title="Mushroom AI Care", page_icon="🍄", layout="wide")

# --- UI 스타일 (이미지 크기 제한 및 버튼 가독성) ---
def apply_custom_css(theme):
    if theme == "Dark (블랙)":
        bg, s_bg, txt, c_bg, bord = "#0e1117", "#1c1e26", "#ffffff", "#262936", "#3e4251"
    else:
        bg, s_bg, txt, c_bg, bord = "#ffffff", "#f0f2f6", "#000000", "#f8f9fa", "#d1d8e0"
    
    st.markdown(f"""
        <style>
        header {{ visibility: hidden; height: 0px !important; }}
        .block-container {{ padding-top: 0px !important; }}
        .stApp {{ background-color: {bg}; color: {txt}; }}
        .main-header {{ background: {c_bg}; padding: 12px; border-radius: 0 0 20px 20px; border: 1px solid {bord}; text-align: center; margin-bottom: 15px; }}
        
        /* 이미지 크기 고정 (스크롤 방지) */
        .stImage img {{ max-height: 400px; object-fit: contain; width: auto !important; margin: 0 auto; display: block; }}
        
        [data-testid="stSidebar"] {{ background-color: {s_bg} !important; }}
        [data-testid="stSidebar"] * {{ color: {txt} !important; }}
        [data-testid="stFileUploader"] button {{ color: {txt} !important; border: 1px solid {bord} !important; }}
        .result-card {{ background: {c_bg}; padding: 10px; border-radius: 10px; border: 1px solid {bord}; margin-bottom: 8px; }}
        .mode-status {{ background: #4A90E2; color: white !important; padding: 5px; border-radius: 5px; text-align: center; font-weight: bold; }}
        </style>
    """, unsafe_allow_html=True)

# --- 사이드바 ---
with st.sidebar:
    st.markdown("### ⚙️ 설정")
    theme = st.radio("🎨 테마", ["Dark (블랙)", "Light (화이트)"])
    st.markdown("---")
    # 민감도를 더 낮게 설정할 수 있도록 조절 (작은 버섯 탐지용)
    conf_v = st.slider("🎯 민감도 (낮을수록 많이 잡음)", 0.01, 1.0, 0.25)
    iou_v = st.slider("📏 중복 제거", 0.1, 0.9, 0.35)
    st.markdown("---")
    mode = st.selectbox("🖥️ 분석 모드", ["📸 사진 분석", "📹 실시간 영상"])
    st.markdown(f'<div class="mode-status">현재: {mode}</div>', unsafe_allow_html=True)

apply_custom_css(theme)

# 2. 모델 로드 (경로 에러 방지)
@st.cache_resource
def load_yolo():
    curr = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(curr, "..", "2. Models", "best.pt")
    if not os.path.exists(path):
        path = "best.pt" # 현재 폴더에 있는 경우
    return YOLO(path)

try:
    model = load_yolo()
except Exception as e:
    st.error("모델 파일을 찾을 수 없습니다.")
    st.stop()

# --- 메인 화면 ---
st.markdown('<div class="main-header"><h2>🍄 표고버섯 AI 스마트 진단</h2></div>', unsafe_allow_html=True)

if mode == "📸 사진 분석":
    col1, col2 = st.columns([1, 1])

    with col1:
        st.write("### 🖼️ 사진 업로드")
        f = st.file_uploader("이미지", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
        if f:
            img = Image.open(f)
            # 작은 버섯 탐지를 위해 iou와 conf 적용
            res = model.predict(img, conf=conf_v, iou=iou_v)
            st.image(res[0].plot(), use_container_width=True)

    with col2:
        st.write("### 📊 진단 리포트")
        if f:
            boxes = res[0].boxes
            st.markdown(f'<div class="result-card"><b>총 탐지:</b> {len(boxes)}개</div>', unsafe_allow_html=True)
            
            for i, box in enumerate(boxes):
                label = model.names[int(box.cls[0])]
                score = float(box.conf[0]) * 100
                
                if label == "Disease":
                    k_name, s_color = "병해(질병)", "#FF5252"
                    detail = "진단 불가"
                elif label == "Culture":
                    k_name, s_color = "모판(배양)", "#4A90E2"
                    detail = f"배양기 ({int(score/30)+1}일차)"
                else: # Growth
                    k_name, s_color = "버섯(생육)", "#4CAF50"
                    # 박스 크기에 따른 생육 일수 보정
                    xyxy = box.xyxy[0].tolist()
                    size = np.sqrt((xyxy[2]-xyxy[0])**2 + (xyxy[3]-xyxy[1])**2)
                    days = int(7 + (size / 60))
                    detail = f"생육 {min(days, 14)}일차"

                st.markdown(f"""
                <div class="result-card">
                    <b>#{i+1} {k_name}</b> <span style="color:{s_color};">●</span><br>
                    <small>확률: {score:.1f}% | {detail}</small>
                </div>
                """, unsafe_allow_html=True)

elif mode == "📹 실시간 영상":
    st.write("### 📹 실시간 관찰 및 상태 진단")
    run = st.toggle("카메라 가동")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        win = st.empty()
    with col2:
        st.write("### 📊 실시간 리포트")
        report_placeholder = st.empty()

    if run:
        vid = cv2.VideoCapture(0)
        cnt = 0 
        # 초기 메시지 설정 (메모리 절약을 위해 단순 문자열 사용)
        last_report = '<div style="color:gray; text-align:center;">버섯을 비춰주세요.</div>'
        
        while run:
            ret, frame = vid.read()
            if not ret: break
            
            cnt += 1
            # 1. 영상 출력 (성능을 위해 2프레임에 한 번만 모델 예측 수행 권장)
            if cnt % 2 == 0:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                res = model.predict(frame_rgb, conf=conf_v, iou=iou_v, verbose=False)
                win.image(res[0].plot(), use_container_width=True)
                
                boxes = res[0].boxes
                
                # 2. 리포트 업데이트 (5프레임에 한 번만 수행하여 메모리 보호)
                if len(boxes) > 0 and cnt % 5 == 0:
                    items = []
                    items.append(f'<div style="background:#4A90E2; color:white; padding:8px; border-radius:10px; margin-bottom:10px; font-weight:bold; text-align:center;">탐지: {len(boxes)}개</div>')
                    
                    # 최대 5개만 처리 (메모리 과부하 방지)
                    for i, box in enumerate(boxes[:5]): 
                        raw_label = model.names[int(box.cls[0])].lower()
                        score = float(box.conf[0]) * 100
                        
                        # 생육 일수 계산
                        xyxy = box.xyxy[0].tolist()
                        size = np.sqrt((xyxy[2]-xyxy[0])**2 + (xyxy[3]-xyxy[1])**2)
                        
                        if 'dis' in raw_label:
                            k_name, s_color, detail = "병해", "#FF5252", "방제 필요"
                        elif 'cul' in raw_label or 'norm' in raw_label:
                            k_name, s_color, detail = "배양", "#4A90E2", "상태 양호"
                        else:
                            k_name, s_color = "생육", "#4CAF50"
                            days = int(7 + (size / 60))
                            detail = f"생육 {min(days, 14)}일차"

                        items.append(f"""
                        <div style="border-left: 4px solid {s_color}; padding:5px 10px; border-radius:5px; margin-bottom:5px; background:rgba(128,128,128,0.05); font-size:13px;">
                            <b>#{i+1} {k_name}</b> | {score:.1f}%<br>
                            <span style="color:#666; font-size:12px;">{detail}</span>
                        </div>
                        """)
                    
                    # 리스트를 합쳐 메모리에 저장
                    last_report = "".join(items)
            
            # 3. 화면 업데이트 (탐지되지 않아도 마지막 결과 유지)
            report_placeholder.markdown(last_report, unsafe_allow_html=True)
                
        vid.release()