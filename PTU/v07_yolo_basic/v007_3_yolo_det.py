from ultralytics import YOLO
import cv2

#  1. 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 추론
model("C:/Users/Administrator/Desktop/PTU/v07_1_yolo_basic/13235238_1080_1920_60fps.mp4")

