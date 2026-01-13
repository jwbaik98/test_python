#  미터(m)를 피트(ft)로 변환하는 함수

# 함수 정의

def meters_to_feet(meters):
    feet = meters * 3.28084
    return feet

# 사용자로부터 문자열 입력
user_input = input("미터 값을 입력해주세요. :")
meters = float(user_input)
# print(type(user_input)) # <clss 'str'>
feet = meters_to_feet(meters)
print(f"{meters}m는 {feet}ft입니다.")

