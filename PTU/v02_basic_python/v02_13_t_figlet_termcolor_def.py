#  pyfiglet + termcolor를 활용한 텍스트 출력 함수


import pyfiglet
from termcolor import colored

# def good_sentence(sentence:str = "Hellow", color:str = "green", on_color:str = None, style:str = ["bold"]) :
#     py_sentence = pyfiglet.figlet_format(sentence)
#     color_sentence = colored(py_sentence, color, on_color, style)
#     print(color_sentence)
    
# good_sentence("good")

# 1. 함수정의(독스트링, 타입 힌트, 기본 값 설정)
def decirate_text(text:str, color:str):
    """
    함수설명 :
        1. pyfiglet으로 텍스트를 튜닝  
        2.  termcolor로 색상적용

    매개변수 :
    
        text (str) : 출력할 문자열
        color (str) : 글자 색상 (예: "red", "blue")
    """
    py_text = pyfiglet.figlet_format(text)
    color_py_text = colored(py_text, color)
    print(color_py_text)
        
# 2. 함수 호출
decirate_text("Hello", "red")