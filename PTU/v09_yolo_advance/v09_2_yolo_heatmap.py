from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
video_path = r"v09_yolo_advance/input.mp4"
cap = cv2.VideoCapture(video_path)

# 2. 모델로드 및 Heatmap 객체 생성
heatmap = solutions.Heatmap(
    model = "yolo11n.pt",
    show = True,
    colormap = cv2.COLORMAP_MAGMA,
)

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("웹캠 읽기 실패 ㅠㅠ")
        break
    
    results = heatmap(frame)
    
     # annotated_frame = results[0].plot()
    
    # cv2.imshow("HEATMAP", annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# 4. 자원 해제 
cap.release()
# cv2.destroyAllWindows()