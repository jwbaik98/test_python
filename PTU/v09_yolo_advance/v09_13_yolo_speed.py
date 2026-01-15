import cv2
from ultralytics import solutions

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv013.stream/playlist.m3u8")

# 2. 속도 추정 객체 생성 및 모델 로드
yolo_speed = solutions.SpeedEstimator(
    model = "yolo11n.pt",
    show = True,
    max_speed = 120,
    meter_per_pixel = 0.1,   # 픽셀 당 실제 이동거리
    classes = [2],
    line_width = 2   # 바운딩 박스 두께
)
 
# 3. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 읽기 실패")
        break
    
    # 3-1. 속도계산 및 추적 수행 
    yolo_speed(frame) 
    
    # 3-2 q키를 눌러서 종료
    if cv2.waitKey(5) & 0xFF == ord('q'):
        print("q키를 눌러서 종료합니다.")
        break
    
# 4. 자원 해제
cap.release()

# 1. 픽셀 당 실제 거리를 얻을 수 있는 방법
# 차선의 5m(추정) 의 각 끝단의 좌표 확인
# 두 좌표 사이의 거리를 구하려면 수학의 피타고라스 정리를 사용하면 됩니다. 
# 화면은 $x$축과 $y$축으로 이루어진 2차원 평면이기 때문입니다.
# 1. 픽셀 거리 계산 공식두 점 $(x_1, y_1)$과 $(x_2, y_2)$ 사이의 거리 $d$는 다음과 같습니다.
    # $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$제공해주신 좌표 $(502, 339)$와 $(519, 357)$을 대입해 보겠습니다.
    # x축 차이: $519 - 502 = 17$
    # y축 차이: $357 - 339 = 18$
    # 계산: $\sqrt{17^2 + 18^2} = \sqrt{289 + 324} = \sqrt{613} 24.76픽셀
# 2. meter_per_pixel 값 구하기이제 실제 거리(5m)를 픽셀 거리(약 24.76px)로 나누면 됩니다.
    #  공식: $Actual\ Distance\ (m) / Pixel\ Distance\ (px)$계산: $5 / 24.76 \approx \mathbf{0.2019}$
    # 따라서, 코드의 meter_per_pixel 인자값에 0.2 정도를 넣으시면 가장 적절합니다.

# 차선의 3m(추정)
    # 1. meter_per_pixel 계산식$$meter\_per\_pixel = \frac{실제 거리 (3m)}{픽셀 거리 (24.76px)} \approx \mathbf{0.1211}$$
    # 따라서 차선이 3m라고 판단된다면, 코드의 설정값을 0.12 정도로 수정하시면 됩니다.