from ultralytics import YOLO
import cv2

# 1. 학습된 모델 로드
model = YOLO('C:/Users/Administrator/Desktop/PTU/runs/detect/mushroom_yolo_v12/weights/best.pt')  # best.pt가 있는 실제 경로 입력

# 2. 이미지 추론 (사진, 영상, 혹은 폴더 전체 가능)
results = model.predict(source='v17_mini_project/test/표고_생육실1_1_18574657.jpg', save=True, conf=0.5)

# 3. 결과 확인
for r in results:
    # 화면에 결과창 띄우기
    im_array = r.plot()  # 결과가 그려진 이미지
    cv2.namedWindow("YOLO Result", cv2.WINDOW_NORMAL)
    cv2.imshow('YOLO Result', im_array)
    cv2.waitKey(0)

cv2.destroyAllWindows()