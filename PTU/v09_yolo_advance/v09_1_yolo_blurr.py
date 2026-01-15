from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture(0)

# 2. 모델 로드
blurrer = solutions.ObjectBlurrer(
    model = "yolo11n.pt",
    show = True,
    blur_ratio = 0.3,
    classes=[0, 39, 67],
    conf = 0.3
)

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("웹캠 읽기 실패")
        break
    
    # 3-1. 예측 수행
    blurrer(frame)   
    
    if cv2.waitKey(1) & 0XFF == ord('q'):
        print("q키를 눌러서 종료합니다.")
        break
    
# 4. 자원 해제
cap.release()