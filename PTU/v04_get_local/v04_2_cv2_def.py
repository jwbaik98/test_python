import cv2   # 컴퓨터 버전
import os    # os 접근 관련
from datetime import datetime   # 날짜 관련
import time

def capture_images():
# 1. 저장 디렉토리 설정
    save_dir = "./captured_images"  # 사진을 저장할 폴더 경로
    os.makedirs(save_dir, exist_ok=True)  # 폴더가 저장

    # 2. 카메라 연결
    # 0은 시스템의 첫 번째 카메라(기본 웹캠)를 의미합니다.
    cap = cv2.VideoCapture(0)

    print("카메라를 준비 중입니다...")
    time.sleep(2)

    # 카메라가 실제로 열렸는지 확인하는 안전장치를 추가하면 더 좋습니다.
    if not cap.isOpened():
        print("카메라를 열 수 없습니다. 연결 상태를 확인하세요.")
        exit() # 카메라가 없으면 프로그램을 종료합니다.

    # 3. 프레임 읽기
    suseess, frame = cap.read()
    if suseess:
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
    
capture_images()


# 위 코드를 함수로 만들어 주세요

# 함수 정의

# def capture_image(save_dir = "./captured_images" ): 
#     os.makedirs(save_dir, exist_ok=True)     
    
#     cap = cv2.VideoCapture(0)       
     
#     suseess, frame = cap.read()
#     if suseess:
#         print("프레임 읽기 성공")
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         file_path = os.path.join(save_dir, f"result_{timestamp}.jpg")
#         cv2.imwrite(file_path, frame)
#         print(f"사진이 저장 됐습니다. {file_path}")
#     else :
#         print("프레임 읽기 실패")    
#     cap.release()
#     cv2.destroyAllWindows()
    
# capture_image()


    