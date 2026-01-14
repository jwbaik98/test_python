from ultralytics import YOLO
import cv2

#  1. 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 추론
model(r"C:/Users/Administrator/Desktop/PTU/v07_1_yolo_basic/13235238_1080_1920_60fps.mp4")

# Ultralytics 공식 문서나 구글링, GPT, Gemini 검색하여 찾아보기

# # 3. 추론 및 분석 영상 저장
# # save=True를 하면 자동으로 박스가 그려진 영상이 저장됩니다.
# results = model.predict(source=r"C:/Users/Administrator/Desktop/PTU/v07_1_yolo_basic/13235238_1080_1920_60fps.mp4", save=True)
results = model.predict(source=r"C:/Users/Administrator/Desktop/PTU/v07_1_yolo_basic/see.mp4", save=True)


# # 4. 텍스트 파일 생성 (물체 이름과 확률만 기록)
# with open("result_summary.txt", "w", encoding="utf-8") as f:
#     f.write("=== 동영상 분석 결과 보고서 ===\n")
    
#     for i, r in enumerate(results):
#         # 해당 프레임에 물체가 하나라도 있을 때만 기록
#         if len(r.boxes) > 0:
#             f.write(f"\n[프레임 {i}] 탐지 결과:\n")
            
#             for box in r.boxes:
#                 # 번호로 된 클래스를 이름으로 변환 (예: 0 -> person)
#                 cls_id = int(box.cls[0])
#                 label = model.names[cls_id]
                
#                 # 확률 계산 (0.95 -> 95.0%)
#                 conf = float(box.conf[0]) * 100
                
#                 # 텍스트 파일에 쓰기
#                 f.write(f" - {label} : {conf:.1f}%\n")

# print("-" * 30)
# print("1. 분석 영상: runs/detect/predict 폴더 확인")
# print("2. 텍스트 결과: result_summary.txt 파일 확인")
# print("-" * 30)