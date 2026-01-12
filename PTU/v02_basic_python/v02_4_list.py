# 리스트 값 변경과 조작
# 특징 : 순서, 수정, 중복 허용

coliors = ["red", "green", "blue"]

# 1. 인덱싱
# print(coliors[0])   # red
# print(coliors[-1])  # blue 순번 맨 마지막 

# 2. 슬라이싱
# print(coliors[0:2])    "red", "green"
# print(coliors[0:-1])   "red", "green"
# print(coliors[1:2])     "green"
# print(coliors[::-1]) ['blue', 'green', 'red']
# print(coliors[::2]) ['red', 'blue']
# print(coliors[:]) ['red', 'green', 'blue']

# 3. 값 변경
# print(coliors[-1])  # blue
# coliors[-1] = "black"
# # print(coliors[-1])  #black

# # 4. 값 추가
# coliors.append("pink")
# print(coliors)

# # 5. 값 추가2
# coliors.insert(0, "white")
# print(coliors)
# # ['white', 'red', 'green', 'black', 'pink']

# # 6. 값 제거
# coliors.remove("white")
# print(coliors)
# # ['red', 'green', 'black', 'pink']


numbers = [1, 25, 3, 14, 5]
# 7. 정렬
# numbers.sort() # 오름차순 정렬 [1, 3, 5, 14, 25]
# print(numbers)
# numbers.sort(reverse=True) # 내림차순 정렬 [25, 14, 5, 3, 1]
# print(numbers)

# 8. 뒤집기
# numbers.reverse() # 반대 정렬 [5, 14, 3, 25, 1]
# print(numbers)

# 9. 리스트 요소 포함 여부 확인
# print(3 in numbers) # True, False 형태로 반환
