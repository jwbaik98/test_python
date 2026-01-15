from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv013.stream/playlist.m3u8")

# 2. 카운팅 구역 설정
count_points = [(227, 407), (574, 314)]

# 클릭된 좌표는 (141, 378) 입니다.
# 클릭된 좌표는 (227, 407) 입니다.
# 클릭된 좌표는 (439, 388) 입니다.
# 클릭된 좌표는 (574, 314) 입니다.

# 3. 모델 로드 및 객체 생성
counter = solutions.ObjectCounter(
    model = "yolo11s.pt",
    show = True,
    region = count_points,
    classes = [3, 5, 7],
    conf = 0.6
)

# 4. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 읽기 실패")
        break

    # 4-1. 프레임 리사이즈
    re_frame = cv2.resize(frame, (640, 480))

    # 4-2. 모델 예측 및 구역 객체 카운팅
    counter(re_frame)
    
    # 4-3. q키를 눌러서 종료
    if cv2.waitKey(5) & 0xFF == ord('q'):
        print("q키를 눌러서 종료합니다.")
        break

# 5. 자원 해제
cap.release()
