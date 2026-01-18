# # 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

# import os
# from huggingface_hub import InferenceClient

# client = InferenceClient(
#     provider="auto",
#     api_key="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",
# )

# # 사용자 입력 받기
# answer = input("생성할 이미지를 설명해주세요 : ")

# # output is a PIL.Image object
# image = client.text_to_image(
#     answer,
#     model="black-forest-labs/FLUX.1-dev",
# )

# # 생성된 이미지 저장
# image.save("tti_result.jpg")

# # 완료 메세지 출력
# print("전체 코드가 잘 실행됐습니다.")

# ---------------------------------------------------------------------------
# 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

import os
from huggingface_hub import InferenceClient
import requests
from urllib.parse import quote

client = InferenceClient(
    provider="auto",
    api_key="",
)

# Google Translate 번역 함수
def google_translate(text):
    """Google Translate를 사용한 한글->영어 번역"""
    try:
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=ko&tl=en&dt=t&q={quote(text)}"
        response = requests.get(url, timeout=10)
        result = response.json()
        translated_text = result[0][0][0]
        return translated_text
    except Exception as e:
        print(f"❌ 번역 실패: {e}")
        return text

# 사용자 입력 받기
user_input = input("생성할 이미지를 설명해주세요 (한글/영어 가능): ")

# 한글 감지
def is_korean(text):
    """한글이 포함되어 있는지 확인"""
    return any('\uac00' <= char <= '\ud7af' for char in text)

# 번역 수행
if is_korean(user_input):
    print(f"\n📝 입력: {user_input}")
    print("🌐 Google Translate로 번역 중...\n")
    
    prompt = google_translate(user_input)
    
    print(f"✅ 번역 완료: {prompt}\n")
else:
    prompt = user_input

print("🎨 이미지 생성 중 (약 1-2분 소요)...\n")

try:
    # 이미지 생성
    image = client.text_to_image(
        prompt,
        model="black-forest-labs/FLUX.1-dev",
    )

    # 생성된 이미지 저장
    image.save("tti_result.jpg")

    # 완료 메세지 출력
    print("✅ 이미지 생성 완료!")
    print("📁 저장 위치: tti_result.jpg")

except Exception as e:
    print(f"❌ 오류 발생: {e}")
    print("💡 API 키를 확인하거나 네트워크 연결을 확인해주세요.")