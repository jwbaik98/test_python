#  변수 값 활용(기초 연산)
a = 9
b = 2
numbers = [1, 2, 3, 4, 5]

# 1. 덧셈
print(a+b)

# 2. 뺄셈
print(a-b)

# 3. 곱셈
print(a*b)

# 4. 나눗셈
print(a/b)

# 5. 몫
print(a//b)

# 6. 나머지
print(a/b)

# 7. 거듭제곱
print(a**b)

result = [i * 2 for i in numbers]
print(result) # [2, 4, 6, 8, 10]
print(sum(numbers))
print(min(a, b))