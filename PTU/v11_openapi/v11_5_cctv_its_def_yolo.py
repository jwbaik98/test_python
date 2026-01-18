from ultralytics import YOLO
import cv2
from v11_4_cctv_its_def import its_cctv

# 1. its_cctv 함수 가져오기
test_url = its_cctv(50)
print(test_url)


# 2. 비디오 경로 설정
cap = cv2.VideoCapture(test_url)

# 3. 모델 로드
model = YOLO("yolo11n.pt")

# 4. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 읽기 실패")
        break
    
    # 4-1. 모델 추론
    results = model(frame)
    
    # 4-2. 결과 시각화
    annotated_frame = results[0].plot()
    
    # 4-3. 결과 시각화 창
    cv2.namedWindow("ITS_YOLO", cv2.WINDOW_NORMAL)
    cv2.imshow("ITS_YOLO", annotated_frame)
    
    # 4-4. q키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('q키를 눌러서 종료')
        break

# 5. 자원 해제
cap.release()
cv2.destroyAllWindows()

# its_cctv 함수에서 매개변수 추가(2가지 이상)