# import streamlit as st
# from ultralytics import YOLO
# import cv2
# import pandas as pd
# import plotly.express as px   # pip install plotly
# import time

# # 1. 화면 구성
# # 좌/우 2개 컬럼 생성
# col1, col2 = st.columns(2)

# with col1:
#     frame_placeholder = st.empty()   # 왼쪽 컴럼 : YOLO 프레임 표시용 빈 영역
    
# with col2:
#     chart_placeholder = st.empty()   # 오른쪽 컴럼 : 객체 수 크래프 표시용 빈 영역
    
# # 2. 비디오 경로 설정
# cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv004.stream/playlist.m3u8")

# # 3. 모델 로드
# model = YOLO("yolo11n.pt")

# # 4. 비디오 프레임 처리
# while cap.isOpened():
#     success, frame = cap.read()
#     if not success:
#         st.warning("CCTV FRAME ERROR")
#         break
    
#     # 4-1. YOLO 모델 객체 탐지 수행
#     results = model(frame)
    
#     # 4-2. 탐지 결과가 그려진 프레임 이미지 생성
#     annotated_frame = results[0].plot()
    
#     # 4-3. 탐지된 객체의 클래스 이름 추출
#     labels = [model.names[int(c)] for c in results[0].boxes.cls] 
    
#     # 4-4. 탐지 객체 수 시각화
#     if labels:  # 탐지된 객체가 있을 경우
#         # labels 리스트를 DataFrame으로 변환 후 객체별 개수 집계
#         df_count = pd.DataFrame({"Object" : labels})
#         df_count = df_count.value_counts().reset_index(name = "Count")
        
#         # Plotly를 이용해 막대 그래프 생성
#         fig = px.bar(
#             df_count,
#             x = "Object",
#             y = "Count",
#             title = "탐지 객체 수",
#             color = "Object",
#             text = "Count"
#         )
#     else: # 탐지된 객체가 없을 경우 빈 그래프 생성
#         df_count = pd.DataFrame({"Object" : [], "Count" : []})
#         fig = px.bar(
#             df_count,
#             x = "Object",
#             y = "Count",
#             title = "탐지 객체 수",     
#         )
    
#     # 4-5. streamlit에 결과 표시
#     frame_placeholder.image(annotated_frame, channels="BGR")
#     chart_placeholder.plotly_chart(fig, use_container_width=True, key=f"chart_{time.time()}") 

# # 5. 자원 해제
# cap.release()
# cv2.destroyAllWindows()


# -----------------------------------------------------------------------------------------------------------

import streamlit as st
from ultralytics import YOLO
import cv2
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime

# 1. 페이지 설정
st.set_page_config(
    page_title="YOLO CCTV 실시간 탐지",
    page_icon="📹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS 스타일 커스터마이징
st.markdown("""
    <style>
        /* 메인 배경색 */
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        /* 제목 스타일 */
        h1 {
            color: white;
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        h2 {
            color: white;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }
        
        /* 메트릭 카드 스타일 */
        .metric-card {
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin: 10px 0;
        }
        
        /* 사이드바 스타일 */
        .sidebar .sidebar-content {
            background: white;
        }
    </style>
""", unsafe_allow_html=True)

# 3. 헤더 영역
st.markdown("<h1>📹 YOLO CCTV 실시간 탐지 시스템</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-size: 16px;'>AI 기반 객체 감지 및 분석</p>", unsafe_allow_html=True)

# 4. 사이드바 설정
with st.sidebar:
    st.markdown("### ⚙️ 설정")
    st.markdown("---")
    
    # 신뢰도 설정
    confidence = st.slider(
        "신뢰도 (Confidence)",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.05,
        help="객체 탐지 신뢰도 임계값"
    )
    
    # 추가 옵션
    st.markdown("---")
    st.markdown("### 📊 표시 옵션")
    show_fps = st.checkbox("⚡ FPS 표시", value=True)
    show_stats = st.checkbox("📈 통계 표시", value=True)
    
    st.markdown("---")
    st.markdown("### ℹ️ 정보")
    st.info("""
    🎯 **기능:**
    - 실시간 객체 탐지
    - 객체별 개수 집계
    - FPS 모니터링
    - 통계 분석
    """)

# 5. 메인 콘텐츠 레이아웃
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🎥 실시간 CCTV 피드")
    frame_placeholder = st.empty()

with col2:
    st.markdown("### 📊 탐지 통계")
    chart_placeholder = st.empty()
    stats_placeholder = st.empty()

# 6. 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv004.stream/playlist.m3u8")

if not cap.isOpened():
    st.error("❌ CCTV 연결 실패!")
    st.stop()

# 7. 모델 로드
with st.spinner("🤖 YOLO 모델 로드 중..."):
    model = YOLO("yolo11n.pt")
st.success("✅ 모델 로드 완료!")

# 8. 통계 추적용 변수
object_history = {}
frame_count = 0
start_time = time.time()
fps_time = time.time()
frame_counter = 0

# 9. 비디오 프레임 처리
try:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            st.warning("⚠️ CCTV 프레임 읽기 실패")
            break
        
        # 9-1. YOLO 모델 객체 탐지
        results = model(frame, conf=confidence)
        
        # 9-2. 탐지 결과 시각화
        annotated_frame = results[0].plot()
        annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        
        # 9-3. 탐지된 객체 정보 추출
        labels = [model.names[int(c)] for c in results[0].boxes.cls]
        
        # 9-4. 통계 업데이트
        for label in labels:
            object_history[label] = object_history.get(label, 0) + 1
        
        frame_count += 1
        frame_counter += 1
        
        # 9-5. FPS 계산
        current_time = time.time()
        elapsed = current_time - fps_time
        if elapsed >= 1.0:
            fps = frame_counter / elapsed
            fps_time = current_time
            frame_counter = 0
        else:
            fps = 0
        
        # 9-6. 그래프 생성
        if labels:
            df_count = pd.DataFrame({"Object": labels})
            df_count = df_count.value_counts().reset_index(name="Count")
            
            fig = px.bar(
                df_count,
                x="Object",
                y="Count",
                title="🎯 현재 탐지 객체 수",
                color="Count",
                color_continuous_scale="Viridis",
                text="Count",
                template="plotly_white"
            )
            
            fig.update_layout(
                height=400,
                showlegend=False,
                hovermode="x unified"
            )
            
            fig.update_traces(textposition="outside")
        else:
            fig = go.Figure()
            fig.add_annotation(
                text="탐지된 객체 없음",
                xref="paper",
                yref="paper",
                x=0.5,
                y=0.5,
                showarrow=False,
                font=dict(size=20, color="gray")
            )
            fig.update_layout(
                height=400,
                title="🎯 현재 탐지 객체 수",
                template="plotly_white"
            )
        
        # 9-7. Streamlit에 결과 표시
        frame_placeholder.image(annotated_frame_rgb, channels="RGB", use_column_width=True)
        chart_placeholder.plotly_chart(fig, use_container_width=True, key=f"chart_{time.time()}")
        
        # 9-8. 통계 표시
        if show_stats:
            with stats_placeholder.container():
                st.markdown("### 📈 실시간 통계")
                
                col_stat1, col_stat2, col_stat3 = st.columns(3)
                
                with col_stat1:
                    st.metric("🎯 현재 객체", len(labels))
                
                with col_stat2:
                    if show_fps:
                        st.metric("⚡ FPS", f"{fps:.1f}")
                
                with col_stat3:
                    elapsed_time = int(time.time() - start_time)
                    st.metric("⏱️ 실행 시간", f"{elapsed_time}초")
                
                # 누적 통계
                if object_history:
                    st.markdown("#### 누적 탐지 통계")
                    sorted_objects = sorted(object_history.items(), key=lambda x: x[1], reverse=True)
                    
                    for obj_name, count in sorted_objects[:5]:  # 상위 5개
                        st.write(f"• **{obj_name}**: {count}회")

except KeyboardInterrupt:
    st.info("🛑 사용자에 의해 중단됨")
except Exception as e:
    st.error(f"❌ 오류 발생: {e}")
finally:
    cap.release()
    cv2.destroyAllWindows()