# 기본적인 변수 타입
# 1. 정수형(Integer)
X = 10
# 정수(소수점 없음) 예) 나이, 개수 등

# 2. 실수형(float)
y = 3.14
# 실수(소수점 있음) 예) 온도, 비율

# 3. 문자형(string)
name = "Python"
name = 'python'
# 문자로 이루어진 데이터 큰따옴표("")/작은따옴표('') 모두 가능

# 4. 불라언(Boolen)
is_python_fun = True
#  true 참, False 거짓

#5. 리스트(List)
coliors = ["red", "green", "blue"]
# 순서가 있고, 변경가능(문자, 숫자)
# 다양한 자료형 섞어도 됨

# 6. 튜플(Tuple)
coords = (10, 20)
# 리스트와 비슷 "수정 불가"의 특징을 가짐

# 7. 딕셔너리(Dictionary)
person = {"name":"Tom", "age":30 }
# {key:value}
# 키(key), 값(value)쌍으로 이루어진 자료형
# JSON처럼 데이터를 구조화할 떄 자주 사용

# 8. 집합(set)
unique_valuse = {1, 2, 3}
# 중복을 허용하지 않음
# 순서가 없음 -> 인덱싱 불가

# 9. NoneType
nothing = None
# "아무것도 없다"는 의미
# 값이 아직 없거나 초기화되지 않은 상태일떄 사용

# 변수 출력
# print(nothing)
# print("nothing의 값:", nothing)
# nothing의 값 : None
# print(type(X))
#  <class 'int'>
# print(isinstance(name, int))

# 실습
# 활용
    # type()
    # isinstance()
Y = 1
N = "Name"
A = [1, 2, 3]
B = "red"
# type(Y)
# type(A)
# isinstance(name, str)
# isinstance(Y, int)