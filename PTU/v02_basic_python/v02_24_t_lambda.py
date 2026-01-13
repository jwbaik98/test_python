# ===============================
# pyfiglet + 함수 + lambda 함수
# ===============================
import pyfiglet
from termcolor import colored

# def good_sentence(sentence:str):
#     '''
#     함수설명 :
#         입력된 문자열을 pyfiglet형식으로 출력합니다.
        
#     매개 변수 :
#          sentence (str) : 출력할 문자열         
#     '''
#     py_sentence = pyfiglet.figlet_format(sentence)
#     print(py_sentence)
    
# # 함수 호출
# good_sentence("------")
# good_sentence("GOOD")
# good_sentence("------")

# # 함수 정의
# good_sentence = lambda sentence : print(pyfiglet.figlet_format(sentence))

# # 함수 호출
# good_sentence("------")
# good_sentence("     GOOD")
# good_sentence("------")

# 일반 함수 정의
# def decorate_text(text):
#     py_text = pyfiglet.figlet_format(text)
#     print(py_text)

# decorate_text("Hello")

decorate_text= lambda text : pyfiglet.figlet_format(text)
py_text = decorate_text("Lambda")
print(py_text)