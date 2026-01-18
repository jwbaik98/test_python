# 1. 허깅페이스에서 원하는 모델 찾기
    # 모델명 : MLP-KTLim/llama-3-Korean-Bllossom-8B

# 2. 찾은 모델로 웹 사이트 구축

# 3. 모델 히스토리 및 정보 탐색
    # - 장점 : 자연스러운 한국어 대화, 한국 문화 상식
    # - 단점 : 복잡한 논리 추론, 전문 지식의 환각 현상


# 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



import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key="",
)

completion = client.chat.completions.create(
    model="MLP-KTLim/llama-3-Korean-Bllossom-8B",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message)