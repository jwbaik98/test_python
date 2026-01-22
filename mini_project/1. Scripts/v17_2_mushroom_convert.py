import json
import os

# -------------------------------학습데이터-----------------------------------------

# # 1. 본인의 v17_mini_project 폴더 절대 경로를 입력하세요.
# PROJECT_PATH = r"C:/Users/Administrator/Desktop/PTU/v17_mini_project"

# def convert_to_yolo_fixed():
#     categories = {'배양': 0, '병해': 1, '생육': 2}
    
#     # 라벨(JSON)이 들어있는 폴더
#     label_base = os.path.join(PROJECT_PATH, "1.Training", "TL5_표고")
#     # 이미지(.jpg)가 들어있는 폴더 (여기에 .txt를 저장할 예정)
#     image_base = os.path.join(PROJECT_PATH, "1.Training", "TS5_표고")
    
#     for cat_name, cat_id in categories.items():
#         json_dir = os.path.join(label_base, cat_name)
#         save_dir = os.path.join(image_base, cat_name)
        
#         if not os.path.exists(json_dir):
#             print(f"폴더 없음: {json_dir}")
#             continue
            
#         json_files = [f for f in os.listdir(json_dir) if f.endswith(".json")]
#         print(f"{cat_name} 카테고리: {len(json_files)}개 변환 시작...")
        
#         for filename in json_files:
#             with open(os.path.join(json_dir, filename), 'r', encoding='utf-8') as f:
#                 data = json.load(f)
            
#             img_w, img_h = data['IMAGE']['WIDTH'], data['IMAGE']['HEIGHT']
#             yolo_data = []
            
#             for anno in data['ANNOTATION_INFO']:
#                 bx = anno['BOUNDING_BOX_X_COORDINATE']
#                 by = anno['BOUNDING_BOX_Y_COORDINATE']
#                 bw = anno['BOUNDING_BOX_WIDTH']
#                 bh = anno['BOUNDING_BOX_HEIGHT']
                
#                 x_center = (bx + bw / 2) / img_w
#                 y_center = (by + bh / 2) / img_h
#                 w_norm, h_norm = bw / img_w, bh / img_h
                
#                 yolo_data.append(f"{cat_id} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}")
            
#             # 파일 쓰기
#             txt_filename = filename.replace(".json", ".txt")
#             with open(os.path.join(save_dir, txt_filename), 'w', encoding='utf-8') as f:
#                 f.write("\n".join(yolo_data))

# convert_to_yolo_fixed()
# print("✅ 진짜로 변환 완료! 탐색기에서 TS5_표고 내부의 카테고리 폴더를 확인하세요.")

# ---------------------------검증 데이터---------------------------------------------


# 1. 본인의 v17_mini_project 폴더 절대 경로를 입력하세요.
PROJECT_PATH = r"C:/Users/Administrator/Desktop/PTU/v17_mini_project"

def convert_to_yolo_fixed():
    categories = {'배양': 0, '병해': 1, '생육': 2}
    
    # 라벨(JSON)이 들어있는 폴더
    label_base = os.path.join(PROJECT_PATH, "2.Validation", "VL5_표고")
    # 이미지(.jpg)가 들어있는 폴더 (여기에 .txt를 저장할 예정)
    image_base = os.path.join(PROJECT_PATH, "2.Validation", "VS5_표고")
    
    for cat_name, cat_id in categories.items():
        json_dir = os.path.join(label_base, cat_name)
        save_dir = os.path.join(image_base, cat_name)
        
        if not os.path.exists(json_dir):
            print(f"폴더 없음: {json_dir}")
            continue
            
        json_files = [f for f in os.listdir(json_dir) if f.endswith(".json")]
        print(f"{cat_name} 카테고리: {len(json_files)}개 변환 시작...")
        
        for filename in json_files:
            with open(os.path.join(json_dir, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            img_w, img_h = data['IMAGE']['WIDTH'], data['IMAGE']['HEIGHT']
            yolo_data = []
            
            for anno in data['ANNOTATION_INFO']:
                bx = anno['BOUNDING_BOX_X_COORDINATE']
                by = anno['BOUNDING_BOX_Y_COORDINATE']
                bw = anno['BOUNDING_BOX_WIDTH']
                bh = anno['BOUNDING_BOX_HEIGHT']
                
                x_center = (bx + bw / 2) / img_w
                y_center = (by + bh / 2) / img_h
                w_norm, h_norm = bw / img_w, bh / img_h
                
                yolo_data.append(f"{cat_id} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}")
            
            # 파일 쓰기
            txt_filename = filename.replace(".json", ".txt")
            with open(os.path.join(save_dir, txt_filename), 'w', encoding='utf-8') as f:
                f.write("\n".join(yolo_data))

convert_to_yolo_fixed()
print("✅ 진짜로 변환 완료! 탐색기에서 TS5_표고 내부의 카테고리 폴더를 확인하세요.")