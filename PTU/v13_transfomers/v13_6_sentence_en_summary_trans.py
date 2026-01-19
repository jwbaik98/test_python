# 1. 라이브러리 불러오기
from transformers import pipeline
from deep_translator import GoogleTranslator

def trans_en_to_ko(sentence) :
    """
    주어진 영어 문장을 한국어로 번역하는 함수
    """
    translated_sen = GoogleTranslator(source = 'en', target = 'ko').translate(sentence)
    return translated_sen


# 2. 요약 파이프라인 생성
summarizer = pipeline(
    "summarization",
    model = "t5-small"
)

# 3. 요약할 영어 문장 입력
text = """
"Nothing in the world can take the place of persistence. Talent will not; nothing is more common than unsuccessful men with talent. Genius will not; unrewarded genius is almost a proverb. Education will not; the world is full of educated derelicts. The slogan 'Press On' has solved and always will solve the problems of the human race.
"""

# 4. 요약문 생성
summary = summarizer(text)

# 5. 요약문 가져오기
sum_text = summary[0]["summary_text"]

# 6. 요약문 출력

# 7. 요약문 번역
# kr_sum_text = GoogleTranslator(source = 'en', target='ko').translate(sum_text)
kr_sum_text = trans_en_to_ko(sum_text)

# 8. 번역된 요약문 출력
print(f"### 요약된 영어문장 : {kr_sum_text} ###")

# -------------------------------------------------------------

# # 1. 라이브러리 불러오기
# from transformers import pipeline
# import requests
# from urllib.parse import quote
# import time

# # 2. 요약 파이프라인 생성
# print("⏳ 요약 모델 로딩 중...")
# summarizer = pipeline(
#     "summarization",
#     model="t5-small",
# )
# print("✅ 요약 모델 로드 완료!\n")

# # 3. Google Translate API를 사용한 번역 함수
# def translate_en_to_ko(text):
#     """Google Translate API를 사용한 영어 -> 한국어 번역"""
#     try:
#         # 문장이 너무 길면 나누기
#         if len(text) > 200:
#             sentences = text.split('. ')
#             translated_sentences = []
            
#             for sentence in sentences:
#                 if sentence.strip():
#                     url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ko&dt=t&q={quote(sentence.strip())}"
#                     response = requests.get(url, timeout=10)
#                     result = response.json()
#                     translated = result[0][0][0]
#                     translated_sentences.append(translated)
#                     time.sleep(0.3)
            
#             return '. '.join(translated_sentences)
#         else:
#             url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ko&dt=t&q={quote(text)}"
#             response = requests.get(url, timeout=10)
#             result = response.json()
#             translated_text = result[0][0][0]
#             return translated_text
            
#     except Exception as e:
#         print(f"❌ 번역 오류: {e}")
#         return text

# # 4. 요약할 영어 문장 입력
# test = """
# "Nothing in the world can take the place of persistence. Talent will not; nothing is more common than unsuccessful men with talent. Genius will not; unrewarded genius is almost a proverb. Education will not; the world is full of educated derelicts. The slogan 'Press On' has solved and always will solve the problems of the human race."
# """

# print("=" * 70)
# print("📄 원본 영어 문장:")
# print("=" * 70)
# print(test)

# # 5. 요약문 생성
# print("\n📝 요약 중...\n")
# summary = summarizer(test)

# # 6. 요약문 가져오기
# sum_text = summary[0]["summary_text"]

# # 7. 영어 요약문 출력
# print("=" * 70)
# print("📌 영어 요약:")
# print("=" * 70)
# print(sum_text)

# # 8. 영어 요약문을 한국어로 번역
# print("\n🌐 한국어로 번역 중...\n")
# korean_summary = translate_en_to_ko(sum_text)

# # 9. 한국어 요약문 출력
# print("=" * 70)
# print("📌 한국어 요약:")
# print("=" * 70)
# print(korean_summary)
# print("=" * 70)