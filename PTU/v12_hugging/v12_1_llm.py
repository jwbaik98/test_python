# 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

# import os
# from huggingface_hub import InferenceClient

# client = InferenceClient(
#     api_key="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",
#     provider="auto"
# )
# # 사용자 질문 입력 받기
# answer = input("질문을 입력해주세요 : ")


# completion = client.chat.completions.create(
#     model="deepseek-ai/DeepSeek-V3.2:novita",
#     messages=[
#         {
#             "role": "user",
#             "content": answer
#         }
#     ],
# )

# # 답변 출력
# print(completion.choices[0].message)


# ---------------------------------------------------

# import os
# from huggingface_hub import InferenceClient
# import re

# client = InferenceClient(
#     api_key="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",
#     provider="auto"
# )

# # 메시지 박스 출력 함수
# def print_message_box(title, message, width=60):
#     """메시지를 박스 형태로 출력"""
#     print("\n" + "="*width)
#     print(f"  {title}")
#     print("="*width)
#     print(f"\n{message}\n")
#     print("="*width + "\n")

# # 사용자 질문 입력 받기
# user_input = input("질문을 입력해주세요: ")

# # 질문 박스 출력
# print_message_box("❓ 질문", user_input)

# completion = client.chat.completions.create(
#     model="deepseek-ai/DeepSeek-V3.2:novita",
#     messages=[
#         {
#             "role": "user",
#             "content": user_input
#         }
#     ],
# )

# # 응답에서 실제 답변만 추출
# response = completion.choices[0].message

# if hasattr(response, 'content'):
#     answer_text = response.content
# else:
#     answer_text = str(response)

# # 답변 박스 출력
# print_message_box("✅ 답변", answer_text)


# ----------------------------------------------------------------------

import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key="",
    provider="auto"
)

# 메시지 박스 출력 함수 (여러 스타일)
def print_box_style1(title, message):
    """스타일 1: 심플한 박스"""
    width = 70
    print("\n" + "█"*width)
    print(f"█ {title:^{width-4}} █")
    print("█"*width)
    print(f"\n{message}\n")
    print("█"*width + "\n")

def print_box_style2(title, message):
    """스타일 2: 둥근 모서리"""
    width = 70
    print("\n" + "┌" + "─"*(width-2) + "┐")
    print(f"│ {title:<{width-4}} │")
    print("├" + "─"*(width-2) + "┤")
    lines = message.split('\n')
    for line in lines:
        print(f"│ {line:<{width-4}} │")
    print("└" + "─"*(width-2) + "┘\n")

def print_box_style3(title, message):
    """스타일 3: 컬러풀한 스타일"""
    width = 70
    print("\n" + "🟦"*35)
    print(f"  {title}")
    print("🟦"*35)
    print(f"\n{message}\n")
    print("🟦"*35 + "\n")

# 사용자 질문 입력 받기
user_input = input("질문을 입력해주세요: ")

# 질문 출력 (스타일 선택)
print_box_style2("❓ 질문", user_input)

print("⏳ 답변을 생성 중입니다...\n")

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3.2:novita",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ],
)

# 응답에서 실제 답변만 추출
response = completion.choices[0].message

if hasattr(response, 'content'):
    answer_text = response.content
else:
    answer_text = str(response)

# 답변 출력 (같은 스타일로)
print_box_style2("✅ 답변", answer_text)