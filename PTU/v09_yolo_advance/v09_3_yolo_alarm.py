from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
stream_url = "http://210.99.70.120:1935/live/cctv007.stream/playlist.m3u8"
cap =  cv2.VideoCapture(stream_url)

# 2. 이메일 인증
from_email = "jwjwbaik98@gmail.com"
password = "icuc mahe zgbx mgus"
to_email = "jwjwbaik98@gmail.com"

# 3. 모델 로드 및 알람 객체 설정
google_alarm = solutions.SecurityAlarm(
    model = "yolo11n.pt",
    show = True,
    records = 3,  # 경고 이메일을 전송하기 위한 최소 감지 수
    classes = [0]
)

# 4. 이메일 서버 인증
google_alarm.authenticate(from_email, password, to_email)

# 5. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("웹캠을 읽지 못 했습니다.")
        break

    google_alarm(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# 6. 자원 해제
cap.release()

# 이메일 알람 문구 변경
# "안녕하세요. 해당 설정하신 객체 탐지됐습니다."

