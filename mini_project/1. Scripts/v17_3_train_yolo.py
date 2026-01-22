from ultralytics import YOLO
import os

def start_training():
    # 1. 모델 로드
    model = YOLO("yolo11n.pt") 

    # 2. 데이터셋 설정 파일의 절대 경로 확인
    # 가급적 역슬래시(\) 대신 슬래시(/)를 사용하세요.
    data_path = "C:/Users/Administrator/Desktop/PTU/v17_mini_project/data.yaml"

    # 3. 학습 시작
    model.train(
        data=data_path, 
        epochs=100,
        patience=15,    # 15번 참아보고 안되면 종료
        imgsz=640,      # 작은 버섯을 잡기 위해 640으로 상향 추천!
        batch=8,        # 메모리 여유가 있다면 8~16 권장
        device='cpu',
        name="mushroom_yolo_v2",
        # 훈련 중간에 문제가 생겨도 이어서 할 수 있도록 설정
        exist_ok=True
    )

if __name__ == '__main__':
    start_training()