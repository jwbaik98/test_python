from ultralytics import YOLO

# 1. 데이터셋 준비
# dataset/ 
# l - train
#      l - class 1(person)/
#                 l - class1.jpg 
#                 l - class1.jpg 
#      l - class2(dog)/
#                 l - class2.jpg        
# l - val/
#      l - class(person)/
#               l - class1.jpg
#               l - class2.jpg
# l - test/  

#  1. 모델 로드
# model = YOLO("yolo11n-cls.pt")

# #  2. 모델 학습
# model.train(
#     data = "dataset", # 데이터셋 경로
#     epochs = 2,  # 학습 횟수
#     batch = 1,  # 배치 사이즈
#     imgsz = 256, # 이미지 크기
# )


# Happy, Sad, Normal 표정 분류 모델
# 이미지 크기 : 256
# 배치 사이즈 : free
# epochs : free

# 가장 우수한 성능 모델에 대해서 

# #  1. 모델 로드
# model = YOLO("yolo11n-cls.pt")

# #  2. 모델 학습
# model.train(
#     data = "dataset", # 데이터셋 경로
#     epochs = 30,  # 학습 횟수
#     batch = 4,  # 배치 사이즈
#     imgsz = 256, # 이미지 크기
#     label_smoothing=0.1,
#     augment=True,        # 기본 증강 활성화
#     mosaic=1.0,          # 4장의 이미지를 합쳐 학습 (데이터 부족 해소)
#     mixup=0.2,           # 이미지 두 장을 겹쳐서 새로운 특징 생성
#     degrees=15.0,        # 고개를 까딱이는 등 약간의 회전 추가
#     flipud=0.0,          # 얼굴이 뒤집히면 안 되니 상하 반전은 0 (좌우 반전은 기본 활성화)
#     patience=10,         # 성능 개선이 없으면 10에폭 후 자동 종료 (Overfitting 방지)
#     workers=2            # CPU 점유율이 너무 높다면 2~4로 설정
# )


# import cv2
# import os
# from datetime import datetime
# from ultralytics import YOLO

# # 1. 모델 로드 및 저장 폴더 생성
# model = YOLO(r"C:/Users/Administrator/Desktop/PTU/runs/classify/train6/weights/best.pt") # 경로 앞에 r을 꼭 붙이세요!
# save_path = "captured_images"
# if not os.path.exists(save_path):
#     os.makedirs(save_path)

# # 2. 웹캠 실행
# cap = cv2.VideoCapture(0)

# print("실행 중... [s]: 사진 저장, [q]: 종료")

# while True:
#     ret, frame = cap.read()
#     if not ret: break

#     # 모델 판별 (학습시 설정한 imgsz와 맞춤)
#     results = model(frame, imgsz=256)
    
#     current_emotion = "Unknown"
#     confidence = 0

#     for r in results:
#         probs = r.probs
#         class_id = probs.top1
#         current_emotion = model.names[class_id]
#         confidence = probs.top1conf.item()

#         # 화면 표시
#         text = f"{current_emotion} ({confidence*100:.1f}%)"
#         cv2.putText(frame, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#     cv2.imshow("Emotion Capture", frame)
#     key = cv2.waitKey(1) & 0xFF

#     # 's' 키를 누르면 사진 저장
#     if key == ord('s'):
#         # 파일명 예시: Happy_20260114_153022.jpg
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"{current_emotion}_{timestamp}.jpg"
#         full_path = os.path.join(save_path, filename)
        
#         cv2.imwrite(full_path, frame)
#         print(f"사진 저장 완료: {full_path}")

#     # 'q' 키를 누르면 종료
#     elif key == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()