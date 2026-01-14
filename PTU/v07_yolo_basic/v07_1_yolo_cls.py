from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("yolo11n-cls.pt")

# 2. 모델 추론
result = model("v07_1_yolo_basic/input8.jpg")

# 3. 결과 확인
result_image = result[0].plot()

# 4. 결과 이미지 저장
output_image_path = "./result8.jpg"
cv2.imwrite(output_image_path, result_image)
print(f"예측 결과 이미지가 잘 저장 되었습니다. {output_image_path}")