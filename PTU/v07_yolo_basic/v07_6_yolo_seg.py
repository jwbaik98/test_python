# from ultralytics import YOLO
# import cv2

# # 1. 웹캠 연결
# cap = cv2.VideoCapture(0)

# # 2. 모델 로드
# model = YOLO("yolo11n-seg.pt")

# # 3. 프레임 처리
# while cap.isOpened():
#     success, fram = cap.read()
#     if not success:
#         print("웹캠 읽기 실패")
#         break
    
#     results = model(fram)
#     annotated_frme = results[0].plot()

#     cv2.imshow("YOLO_SEG", annotated_frme)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         print("q키를 눌러서 종료")
#         break


# # 4. 자원해제
# cap.release()
# cv2.destroyAllWindows()

from ultralytics import YOLO
import cv2

# 1. 모델 로드 및 웹캠 연결
model = YOLO("yolo11n-seg.pt")
cap = cv2.VideoCapture(0)

# --- 영상 저장을 위한 설정 ---
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 카메라 가로 크기
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 카메라 세로 크기
fps = 20                                          # 초당 프레임 수
fourcc = cv2.VideoWriter_fourcc(*'XVID')          # 비디오 코덱 설정
out = cv2.VideoWriter('output_seg.avi', fourcc, fps, (width, height))
# ----------------------------

print("실행 중... [s]: 사진 저장, [q]: 종료")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    # 모델 추론 (Segmentation 실행)
    results = model(frame)
    
    # 결과가 그려진 프레임 만들기
    annotated_frame = results[0].plot()

    # 1. 영상 파일에 현재 프레임 기록
    out.write(annotated_frame)

    # 화면 표시
    cv2.imshow("YOLO_SEG", annotated_frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    # 2. 's' 키를 누르면 사진 저장
    if key == ord('s'):
        cv2.imwrite("captured_seg.jpg", annotated_frame)
        print("사진이 저장되었습니다!")

    # 'q' 키를 누르면 종료
    elif key == ord('q'):
        break

# 4. 자원 해제 (중요: out.release()가 빠지면 영상 파일이 안 열릴 수 있음)
cap.release()
out.release() 
cv2.destroyAllWindows()