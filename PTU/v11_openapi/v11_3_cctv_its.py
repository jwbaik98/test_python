import urllib             # URL 요청
import json               # JSON 데이터 처리용
import pandas as pd       #  데이터 프레임 생성 및 데이터 처리용
import urllib.request     # URL 요청 2
from ultralytics import YOLO
import cv2

# 1. 인증 키 설정
key = "db5c00dc1fce45c49049bff225a0fea6"

# 2. 도로 유형 지정
Type = "its"
# its : 일반도로
# ex : 고속도로

# 3. 관심 영역 설정(경도, 위도)
minX = float(120.95)   # 최소 경도
maxX = float(127.02)   # 최대 경도
minY = float(30.55)    # 최소 위도
maxY = float(37.69)    # 최대 위도

# 4. 응답 데이터 형식 설정
getType = "json"

# 5. API 요청 URL 생성
url_cctv = (
    f"https://openapi.its.go.kr:9443/cctvInfo?apiKey={key}&type={Type}&cctvType=1&minX={minX}&maxX={maxX}&minY={minY}&maxY={maxY}&getType={getType}"
    )

# 6. API 요청 및 응답 받기
response = urllib.request.urlopen(url_cctv)

# 7. 응답 데이터 디코딩 -> bytes -> str
json_str = response.read().decode("utf-8")
# print(json_str)

# 8. JSON 문자열 - >  파이썬 딕셔너리
json_object = json.loads(json_str)
print(json_object)

# 9. 데이터 프레임 변환
cctv_play = pd.json_normalize(json_object["response"]["data"], sep = '')
# print(cctv_play)

# 10. 특정 CCTV 선택
test_url = cctv_play["cctvurl"][1000]
print(f"선택된 CCTV URL : {test_url}")

# 11. 경로 설정
cap = cv2.VideoCapture(test_url)

# 12. 모델 로드
model = YOLO("yolo11n.pt")

# 13. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 읽기 실패")
        break
    
    # 13-1. 모델 예측
    results = model(frame)
    
    # 13-2. 결과 시각화
    annotated_frame = results[0].plot()
    
    # 13-3. 결과 시각화 창 생성
    cv2.namedWindow("OPENAPI", cv2.WINDOW_NORMAL)
    cv2.imshow("OPENAPI", annotated_frame)
    
    # 13-4. q키를 눌러서 종료
    if cv2.waitKey(1) & 0XFF == ord("q"):
        print("q키를 눌러서 종료")
        break
    
# 14. 자원 해제
cap.release()
cv2.destroyAllWindows()