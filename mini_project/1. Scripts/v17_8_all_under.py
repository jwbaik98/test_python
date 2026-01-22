import os
import random

def undersample_class(target_path, target_count):
    # 이미지 파일 리스트 확보
    images = [f for f in os.listdir(target_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    current_count = len(images)
    if current_count <= target_count:
        print(f"  └ ✅ {os.path.basename(target_path)}: 이미 {current_count}개 이하입니다. (작업 건너뜀)")
        return

    # 삭제할 파일 선정
    num_to_delete = current_count - target_count
    to_delete = random.sample(images, num_to_delete)
    
    count = 0
    for img_name in to_delete:
        img_path = os.path.join(target_path, img_name)
        label_name = os.path.splitext(img_name)[0] + ".txt"
        label_path = os.path.join(target_path, label_name)

        try:
            if os.path.exists(img_path): os.remove(img_path)
            if os.path.exists(label_path): os.remove(label_path)
            count += 1
        except Exception as e:
            print(f"  └ ⚠️ 오류 발생 ({img_name}): {e}")
            
    print(f"  └ 🧹 {os.path.basename(target_path)}: {count}세트 삭제 완료 (남은 이미지: {target_count}장)")

# --- 설정부 ---
# 1. 상위 경로 설정 (본인의 환경에 맞게 수정하세요)
root_paths = [
    r"C:/Users/Administrator/Desktop/PTU/v17_mini_project/1.Training/TS5_표고",
    r"C:/Users/Administrator/Desktop/PTU/v17_mini_project/2.Validation/VS5_표고" # Validation 경로 추가
]

# 2. 대상 카테고리 및 목표 수치
categories = ["병해", "배양", "생육"]
target_limit = 500

# --- 실행부 ---
print("🚀 언더샘플링 작업을 시작합니다...")

for root in root_paths:
    print(f"\n📂 대분류 작업 중: {os.path.basename(root)}")
    for category in categories:
        full_path = os.path.join(root, category)
        
        if os.path.exists(full_path):
            undersample_class(full_path, target_limit)
        else:
            print(f"  └ ❌ 폴더를 찾을 수 없음: {category}")

print("\n✨ 모든 작업이 성공적으로 완료되었습니다!")