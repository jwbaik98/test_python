from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
stream_url = "http://210.99.70.120:1935/live/cctv007.stream/playlist.m3u8"
cap =  cv2.VideoCapture(stream_url)

# 2. 모델 로드
model = YOLO("yolo11s.pt")
# 모델크기 n -> s- > m -> l -> x

# 3. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 읽기 실패")
        break
    
    # 객체 추적 수행
    results = model.track(frame, persist = True, classes = [0, 2, 5], conf = 0.7)
    # presist = True -> 이전 프레임 정보 유지

    # 추적 결과 시각화
    annotated_frame = results[0].plot()

    # 결과 화면 조절
    cv2.namedWindow("YOLO_TRACKING", cv2.WINDOW_NORMAL)

    #  결과 화면 출력
    cv2.imshow("YOLO_TRACKING", annotated_frame)
    
    # q키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키를 눌러서 종료")
        break

# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()