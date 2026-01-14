from ultralytics import YOLO
import cv2

# 1. CCTV 스트리밍 url 설정
stream_url = "http://210.99.70.120:1935/live/cctv003.stream/playlist.m3u8"
cap = cv2.VideoCapture(stream_url)

# 2. 모델 로드
model = YOLO("yolo11x.pt")

# 3. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("CCTV URL 확인 또는 웹캠 확인해주세요")
        break
    
    results = model(frame)
    annotated_frame = results[0].plot()

    cv2.imshow("CCTV URL", annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키를 눌러서 종료")
        break

# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()