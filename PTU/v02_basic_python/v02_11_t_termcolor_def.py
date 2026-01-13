# termclolr를 활용한 텍스트 출력 함수 실습

import pyfiglet
from termcolor import colored

# test_colors = colored(
#     "test colors",
#     "blue",
#     "on_white",
#     ["bold"]
# )

# print(test_colors)

# def good_sentence(sentence):
#     py_sentence = pyfiglet.figlet_format(sentence)
#     print(py_sentence)
   
    
# def good_sentence(sentence, color= "red", on_color="blue", attr=None):
#     py_sentence = pyfiglet.figlet_format(sentence)
#     colored_sentence = colored(py_sentence, color=color, on_color=on_color, attrs=[attr] if attr else [])
#     print(colored_sentence)

# # 함수 정의 시 color, attr 등을 받을 수 있게 '구멍'을 뚫어줘야 합니다.
# def good_sentence(sentence, color="white", attr=None):
#     # pyfiglet으로 글자 모양 만들기
#     py_sentence = pyfiglet.figlet_format(sentence)
    
#     # colored 함수에 전달받은 color와 attr 적용하기
#     # attrs는 리스트([]) 형태를 원하므로 조건문을 씁니다.
#     colored_sentence = colored(py_sentence, color=color, attrs=[attr] if attr else [])
    
#     print(colored_sentence)

# # 이제 아래 코드가 정상 작동합니다!
# good_sentence("Success", color="green", attr="bold")

# 함수 정의
def print_colored(sentence:str = "hellow", color = None, on_color = None, style:list = None):
    '''
    텍스트를 원하는 색상, 배경색, 스타일로 출력하는 함수
    
    매개 변수 : 
     sentence(str) : 출력할 문자열
     color(str) : 글자 색상
     on_color(str) : 글자 배경색
     style(str) : 글자 스타일
    '''
    color_sentence = colored(sentence, 
                             color, 
                             on_color, 
                             style)
    print(color_sentence) 

print_colored("Hello", "red", "on_yellow", ["bold"])