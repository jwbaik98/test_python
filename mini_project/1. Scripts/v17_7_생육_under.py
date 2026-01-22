import os
import random

def undersample_class(target_path, target_count):
    # 1. 이미지 파일 리스트 확보
    images = [f for f in os.listdir(target_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    print(f"현재 폴더 내 이미지 개수: {len(images)}")

    if len(images) <= target_count:
        print(f"✅ 현재 개수가 목표({target_count})보다 적거나 같아 작업을 건너뜁니다.")
        return

    # 2. 삭제할 파일 선정
    num_to_delete = len(images) - target_count
    to_delete = random.sample(images, num_to_delete)
    
    print(f"🧹 {num_to_delete}개의 파일을 삭제하여 {target_count}개로 맞춥니다...")

    count = 0
    for img_name in to_delete:
        # 이미지 파일 전체 경로
        img_path = os.path.join(target_path, img_name)
        # 라벨 파일 전체 경로 (이미지와 같은 폴더 내 .txt)
        label_name = os.path.splitext(img_name)[0] + ".txt"
        label_path = os.path.join(target_path, label_name)

        try:
            # 이미지 삭제
            if os.path.exists(img_path):
                os.remove(img_path)
            
            # 라벨 삭제
            if os.path.exists(label_path):
                os.remove(label_path)
            
            count += 1
        except Exception as e:
            print(f"파일 삭제 중 오류 발생 ({img_name}): {e}")
            
    print(f"✅ 정리 완료: 총 {count}세트의 이미지와 라벨을 삭제했습니다.")
    print(f"최종 남은 이미지 개수: {len(os.listdir(target_path)) // 2} (이미지+라벨 합산 기준)")

# --- 실제 실행부 ---
# 텍스트 파일이 이미지와 같이 들어있는 TS5 경로를 지정합니다.
growth_path = r"C:/Users/Administrator/Desktop/PTU/v17_mini_project/1.Training/TS5_표고/생육"
undersample_class(growth_path, 15000)