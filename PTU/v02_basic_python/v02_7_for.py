# # for문 활용
# # 하나씩 꺼내면서 반복 작업을 수행

# mixed = [1, "hellow", 3.14, True]
# # # 기본 리스트 반복문
# # for i in mixed:
# #     print(i)

# # 1
# # hellow
# # 3.14
# # True
    
# # enumerate 사용하기
# for index, i in enumerate(mixed):
#     print(f"index : {index}. : i : {i}")

numbers = [1, 25, 3, 14, 5]

# 모든 요소에 10을 더함 (결과를 다시 리스트로 감싸줘야 함)
result = list(map(lambda x: x + 10, numbers))
print(result)  # [11, 35, 13, 24, 15]