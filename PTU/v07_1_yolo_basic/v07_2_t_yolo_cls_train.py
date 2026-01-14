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

#  1. 모델 로드
model = YOLO("yolo11n-cls.pt")

#  2. 모델 학습
model.train(
    data = "dataset", # 데이터셋 경로
    epochs = 30,  # 학습 횟수
    batch = 4,  # 배치 사이즈
    imgsz = 256, # 이미지 크기
)