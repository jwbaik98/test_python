from ultralytics import YOLO
import os

def start_training():
    # 1. 모델 로드
    model = YOLO("yolo11n.pt") 

    # 2. 학습 시작
    model.train(
        data="C:/Users/Administrator/Desktop/PTU/v17_mini_project/data.yaml", 
        epochs=10,
        imgsz=640,
        batch=4,
        device='cpu',
        name="mushroom_yolo_v1"
    )

if __name__ == '__main__':
    start_training()