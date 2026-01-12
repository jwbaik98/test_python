#  pyfiglet + termcolor를 활용한 텍스트 출력 함수

# 1. 함수정의(독스트링, 타입 힌트, 기본 값 설정)
# 2. 함수 호출

import pyfiglet
from termcolor import colored

def good_sentence(sentence:str = "Hellow", color:str = "green", on_color:str = None, style:str = ["bold"]) :
    py_sentence = pyfiglet.figlet_format(sentence)
    color_sentence = colored(py_sentence, color, on_color, style)
    print(color_sentence)
    
good_sentence("good")