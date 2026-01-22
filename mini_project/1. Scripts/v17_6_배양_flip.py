import cv2
import os
import numpy as np

def augment_by_flipping(image_dir, label_dir):
    # 이미지 리스트 가져오기
    images = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
    print(f"찾은 이미지 개수: {len(images)}")
    
    count = 0
    for img_name in images:
        if img_name.startswith("flip_"): continue 
        
        img_path = os.path.join(image_dir, img_name)
        label_path = os.path.join(label_dir, os.path.splitext(img_name)[0] + ".txt")
        
        if not os.path.exists(label_path):
            continue

        # --- 한글 경로 대응 이미지 읽기 ---
        img_array = np.fromfile(img_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        
        if img is None: 
            print(f"파일을 읽을 수 없음: {img_name}")
            continue
        
        # 좌우 반전
        flipped_img = cv2.flip(img, 1) 
        new_img_name = "flip_" + img_name
        new_img_path = os.path.join(image_dir, new_img_name)

        # --- 한글 경로 대응 이미지 저장 ---
        result, encoded_img = cv2.imencode('.jpg', flipped_img)
        if result:
            encoded_img.tofile(new_img_path)

        # 2. 라벨 파일 수정
        with open(label_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        for line in lines:
            parts = line.split()
            if len(parts) < 5: continue
            cls, x, y, w, h = parts
            new_x = 1.0 - float(x)
            new_lines.append(f"{cls} {new_x} {y} {w} {h}\n")
            
        with open(os.path.join(label_dir, "flip_" + os.path.splitext(img_name)[0] + ".txt"), 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        count += 1

    print(f"✅ 작업 완료: {count}개의 데이터가 증강되었습니다.")

# --- 실행부 ---
target_path = r"C:/Users/Administrator/Desktop/PTU/v17_mini_project/1.Training/TS5_표고/배양"
augment_by_flipping(target_path, target_path)