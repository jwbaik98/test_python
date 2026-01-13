# # kg to pound 변환하는 함수 실습

# # 함수 정의
# def kg_to_pound(kg):
#     pound = kg * 2.20462
#     return pound

# #  사용자로부터 입력
# user_input = input("kg을 입력해주세요: ")


# #  함수 출력
# try:
#     kg = float(user_input)
#     pound = kg_to_pound(kg)
#     print(f"{kg}kg은 {pound:.3f}pound 입니다.")

# except ValueError:
#     # 2. 숫자가 아니라서 에러가 나면 이쪽으로 점프!
#     print("오류: 숫자만 입력할 수 있습니다. 문자는 넣지 마세요.")

import streamlit as st

# 1. 함수 정의
def kg_to_pound(kg):
    return kg * 2.20462

# 2. 웹사이트 화면 구성
st.title("⚖️ 몸무게 변환기 (kg → pound)")
st.write("kg을 입력하면 파운드(lb)로 계산해드립니다.")

# 3. 사용자 입력 (웹의 입력창 사용)
user_input = st.text_input("kg을 입력해주세요:", placeholder="예: 70")

# 4. 버튼 클릭 시 계산 실행
if st.button("변환하기"):
    if user_input:
        try:
            kg = float(user_input)
            
            if kg < 0:
                st.warning("⚠️ 무게는 음수가 될 수 없습니다!")
            else:
                pound = kg_to_pound(kg)
                # 결과를 웹 화면에 예쁘게 표시
                st.success(f"✅ 결과: **{kg}kg**은 **{pound:.3f} pound** 입니다.")
                
        except ValueError:
            st.error("❌ 오류: 숫자만 입력할 수 있습니다. 문자는 넣지 마세요.")
    else:
        st.info("숫자를 먼저 입력해 주세요.")