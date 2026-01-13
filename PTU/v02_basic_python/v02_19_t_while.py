#  kg -> 1b 변환 프로그램(입력 반복, 예외처리)
#  def, while, try, except  사용

def kg_to_pound(kg):
    pound = kg * 2.20462
    return pound

while True:  
    #  사용자로부터 입력
    user_input = input("kg을 입력해주세요. ): ")

    #  예외처리
    try:
        kg = float(user_input)
        pound = kg_to_pound(kg)
        print(f"{kg}kg은 {pound:.3f}pound 입니다.")
        break
    except ValueError:
        print("문자는 넣지 마세요.")