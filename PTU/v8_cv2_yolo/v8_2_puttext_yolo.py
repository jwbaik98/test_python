from ultralytics import YOLO
import cv2

# 1. CCTV 스트리밍 URL 설정
stream_url = "http://210.99.70.120:1935/live/cctv007.stream/playlist.m3u8"
cap = cv2.VideoCapture(stream_url)

# 2. YOLO 모델 로드
model = YOLO("yolo11s.pt")

# 3. 실시간 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("웹캠을 못 읽었습니다.")
        break
    # 3-1. YOLO 객체 탐지
    results = model(frame, classes=[0, 1, 3, 5, 7], conf=0.5)
    
    # 3-2. 탐지 결과 시각화(박스 및 클레스 레벨)
    annotated_frame = results[0].plot()
    
    # 3-3. 탐지된 객체 정보
    boxes = results[0].boxes

    # 3-4. 탐지된 객체 수 계산
    count = len(boxes.cls)
    
    # 3-5. 탐지 갯수에 따른 상태 메세지 결정
    if count >= 10:
        status = "Danger"
        color = (0,0, 255) # 빨강
    
    elif count >= 7:
        status = "Warning"
        color = (0, 255, 0) # 초록
        
    elif count >= 3:
        status = "Normal"
        color = (0, 0, 0) # 검정
    else:
        status = "Safe"
        color = (255, 0, 0) # 파랑

     # 3-6. 탐지 객체 수 및 상태 화면 표시
    cv2.putText(
        annotated_frame,  #  표시할 영상
        f"Detected : {count}, {status}", # 표시 문자열
        (10, 30),  # 좌측 상단 위치
        cv2.FONT_HERSHEY_SIMPLEX,
        1,   #  폰트 크기
        color,  # 글자색
        2,  # 글자 두께
        cv2.LINE_AA,  # 안티앨리어싱 적용
     )   
     
    #  3-7. Opencv 윈도우 출력
    cv2.imshow("CCTV Detection", annotated_frame)
    
    # 3-8. q키를 눌러서 종료
    if cv2.waitKey(1) & 0XFF == ord('q'):
        print("q키를 눌러서 종료합니다.")
        break
    
# 4. 자원해제
cap.release()
cv2.destroyAllWindows()