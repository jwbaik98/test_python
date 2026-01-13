import pyfiglet
from termcolor import colored
# import tkinter.messagebox as msg

# 1. 함수정의
def decorate_text(text, color):
    '''
    1. pyfiglet으로 텍스트를 튜닝
    2. termcolor로 색상 적용
    '''
    py_text = pyfiglet.figlet_format(text)
    color_py_text = colored(py_text, color)
    # print(color_py_text)
    return color_py_text
    
# 2. 함수호출
# print(decorate_text("GOOD", "red"))
# result = decorate_text("GOOD", "red")
# print(result)
# msg.showinfo("결과 확인", result)

# 1. 텍스트 출력 완성
# 2. return을 사용하는 이유
    # 1) 함수의 실행 결과 값을 함수 밖으로 전달할 수 있음.
    #  print()는 값을 화면에 뿌리고 사라지지만, return은 결과값을 변수에 저장하게 하여 저장된 값은 다른 계산이나 함수의 입력값으로 다시 쓸 수 있음.
    # 2) 함수 재사용성과 확장성이 높아짐. 
    #  결과물이 데이터 타입(문자열, 리스트, 숫자 등) 그대로 유지되어 코드 수정에 보다 용이함.
    
last_text = decorate_text("LAST", "yellow")

def box_print(text):
    print("="*40)
    print(text)
    print("="*40)
    
box_print(last_text)

test_text = decorate_text("test", "red")

def box_print(text):
    print("*"*40)
    print(text)
    print("*"*40)
    
box_print(test_text)