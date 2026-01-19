import pytesseract
from PIL import Image
import os

# 1. Tesseract 실행 파일 경로 지정
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

# 2. 이미지 불러오기
image = Image.open("v14_ocr/image5.jpg")

# 3.ocr 수행
results = pytesseract.image_to_string(
    image,
    lang='eng'
)

# 4. 결과 출력
print(results)
# Optical Character
# Recognition(OCR)

# 이미지 1~5번 인식 X, 6, 7(일부 오류인식) 인식

# https://github.com/UB-Mannheim/tesseract/wiki


# import pytesseract
# from PIL import Image
# import cv2
# import numpy as np
# import os
# import re

# pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

# # 텍스트 정제 및 검증 함수
# def clean_and_validate_text(text, min_word_length=2, min_text_length=3):
#     """OCR 결과 정제 및 검증"""
    
#     # 1. 특수문자 제거
#     text = re.sub(r'[^a-zA-Z0-9\s\-_.]', '', text)
    
#     # 2. 여러 공백을 하나로
#     text = re.sub(r'\s+', ' ', text)
    
#     # 3. 앞뒤 공백 제거
#     text = text.strip()
    
#     # 4. 너무 짧은 단어 제거
#     words = text.split()
#     words = [w for w in words if len(w) >= min_word_length]
#     text = ' '.join(words)
    
#     # 5. 최소 길이 확인
#     if len(text) < min_text_length:
#         return None
    
#     # 6. 숫자만 있는 경우 제외
#     if text.replace(' ', '').replace('-', '').replace('_', '').replace('.', '').isdigit():
#         return None
    
#     return text

# image_path = "v14_ocr/image2.jpg"

# if os.path.exists(image_path):
#     img = cv2.imread(image_path)
#     print(f"✅ 이미지 로드 완료\n")
    
#     # 전처리
#     print("📝 전처리 중...\n")
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     scale = 2
#     h, w = gray.shape
#     gray = cv2.resize(gray, (w * scale, h * scale), interpolation=cv2.INTER_CUBIC)
    
#     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#     enhanced = clahe.apply(gray)
    
#     _, thresh = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
#     morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
#     morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)
    
#     denoised = cv2.fastNlMeansDenoising(morph, h=10)
#     pil_image = Image.fromarray(denoised)
    
#     # OCR 수행
#     print("🔍 OCR 수행 중...\n")
    
#     psm_values = [3, 6, 7, 11]
#     valid_results = []
    
#     for psm in psm_values:
#         config = f'--oem 3 --psm {psm}'
#         raw_result = pytesseract.image_to_string(pil_image, lang='eng', config=config)
#         cleaned = clean_and_validate_text(raw_result)
        
#         if cleaned:
#             valid_results.append((psm, cleaned))
#             print(f"✅ PSM {psm}: {cleaned}")
    
#     print("\n" + "=" * 70)
    
#     if valid_results:
#         # 최고의 결과 선택
#         best = max(valid_results, key=lambda x: len(x[1]))
#         print(f"📌 인식된 텍스트 (PSM {best[0]}):")
#         print("=" * 70)
#         print(best[1])
#         print("=" * 70)
#     else:
#         print("❌ 유효한 텍스트를 인식하지 못했습니다.")
#         print("=" * 70)
        
# else:
#     print(f"❌ 파일을 찾을 수 없습니다: {image_path}")