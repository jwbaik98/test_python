import cv2   # 컴퓨터 버전
import os    # os 접근 관련
from datetime import datetime   # 날짜 관련
import schedule
import time

#  사진 캡쳐 간격 설정
inveral_time = 5

def capture_images():
# 1. 저장 디렉토리 설정
    save_dir = "./captured_images"  # 사진을 저장할 폴더 경로
    os.makedirs(save_dir, exist_ok=True)  # 폴더가 저장

    # 2. 카메라 연결
    # 0은 시스템의 첫 번째 카메라(기본 웹캠)를 의미합니다.
    cap = cv2.VideoCapture(0)

    # 3. 프레임 읽기
    success, frame = cap.read()
    if success:
        print("프레임 읽기 성공")

        #  현재 시간 기반 파일명 생성
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(save_dir, f"result_{timestamp}.jpg")

        # 이미지 파일 저장
        cv2.imwrite(file_path, frame)
        print(f"사진이 저장 됐습니다. {file_path}")
    else :
        print("프레임 읽기 실패")
        
    # 4. 자원 해제
    cap.release()
    cv2.destroyAllWindows()
    
#  스케쥴러 설정
schedule.every(inveral_time).seconds.do(capture_images)
print(f"{inveral_time}초 간격으로 데이터를 수집합니다.")

#  스케쥴러 실행
while True:
    schedule.run_pending() # 예약된 작업 실행
    time.sleep(1) # 1초간 대기