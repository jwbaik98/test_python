from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("yolo11x.pt")

# # 모델 클래스 확인
# # print(f"모델 클래스 목록 : {model.name}")
# # print(model.names)

# # 찾고 싶은 물체의 이름 리스트
# target_names = ['cell phone', 'book']

# # 이름에 해당하는 번호(ID) 추출
# # model.names는 {0: 'person', 1: 'bicycle', ...} 형태입니다.
# target_ids = [k for k, v in model.names.items() if v in target_names]

model(
    "v07_yolo_basic/class.jpg",
    save = True,
    # classes=target_ids,
    classes=[67, 73],  # 67: cell phone, 73: book
    conf=0.25,          # 확신도가 25% 이상인 것만 표시
    # max_det=2,
    # save_crop = True, 
    # save_txt=True,
    # save_conf=True
)

# 결과 이미지
# cell phone, book만 탐지되도록