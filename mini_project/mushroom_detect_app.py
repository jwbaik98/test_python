import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

# 1. 페이지 설정
st.set_page_config(page_title="표고버섯 건강 진단 AI", page_icon="🍄", layout="wide")

st.title("🍄 표고버섯 AI 진단 & 실시간 모니터링")
st.markdown("---")

# 2. 모델 로드 (학습된 best.pt 경로 입력)
@st.cache_resource # 모델을 한 번만 로드하도록 캐싱
def load_model():
    return YOLO('yolo11n.pt') # 파일명이 다르면 수정하세요

model = load_model()

# 사이드바 설정
st.sidebar.header("🔍 진단 설정")
app_mode = st.sidebar.selectbox("모드 선택", ["이미지 업로드 진단", "실시간 웹캠 모니터링"])

# --- 모드 1: 이미지 업로드 ---
if app_mode == "이미지 업로드 진단":
    st.subheader("📸 이미지 업로드 진단")
    uploaded_file = st.file_uploader("버섯 사진을 선택하세요...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # 이미지 열기
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(image, caption="원본 이미지", use_container_width=True)
            
        with col2:
            # 예측 실행
            results = model(image)
            res_plotted = results[0].plot() # 박스 그려진 이미지
            st.image(res_plotted, caption="AI 진단 결과", use_container_width=True)
            
            # 탐지 결과 텍스트 출력
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])
                    st.success(f"감지됨: **{model.names[cls]}** (신뢰도: {conf:.2f})")

# --- 모드 2: 실시간 웹캠 ---
elif app_mode == "실시간 웹캠 모니터링":
    st.subheader("📹 실시간 모니터링 중...")
    run = st.checkbox('웹캠 켜기/끄기')
    FRAME_WINDOW = st.image([]) # 실시간 영상을 보여줄 공간
    
    cap = cv2.VideoCapture(0)

    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("카메라를 찾을 수 없습니다.")
            break
            
        # BGR을 RGB로 변환 (OpenCV와 Streamlit 호환용)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # 모델 예측
        results = model(frame)
        annotated_frame = results[0].plot()
        
        # 화면 업데이트
        FRAME_WINDOW.image(annotated_frame)
    else:
        st.write("웹캠이 꺼져 있습니다.")