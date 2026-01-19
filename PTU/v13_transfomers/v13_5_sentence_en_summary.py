from transformers import pipeline

# 1. 요약 파이프라인 생성
summarizer = pipeline(
    "summarization",     # 요약 테스크 지정
    model = "t5-small",
       
)

# 2. 요약할 긴 문장 입력
test = """
"Nothing in the world can take the place of persistence. Talent will not; nothing is more common than unsuccessful men with talent. Genius will not; unrewarded genius is almost a proverb. Education will not; the world is full of educated derelicts. The slogan 'Press On' has solved and always will solve the problems of the human race."
"""

# 3. 요약문 생성
summary = summarizer(test)

# 4. 요약문 가져오기
sum_text = summary[0]["summary_text"]

# 5. 요약문 출력
print("##########################################")
print(f"요약된 문장 : {sum_text}")