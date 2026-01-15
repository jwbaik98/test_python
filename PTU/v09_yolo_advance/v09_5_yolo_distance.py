from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("v09_yolo_advance/input.mp4")

# 2. 모델 로드 및 객체 생성
distance = solutions.DistanceCalculation(
    model = "yolo11n.pt",
    show = True,
)

# 3. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 읽기 실패")
        break
    
    distance(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키를 눌러서 종료")
        break

# 4. 자원 해제
cap.release()