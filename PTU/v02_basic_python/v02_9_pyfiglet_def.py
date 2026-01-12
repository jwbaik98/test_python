import pyfiglet

def good_sentence(sentence:str):
    '''
    함수설명 :
        입력된 문자열을 pyfiglet형식으로 출력합니다.
        
    매개 변수 :
         sentence (str) : 출력할 문자열         
    '''
    py_sentence = pyfiglet.figlet_format(sentence)
    print(py_sentence)
    
# 함수 호출
good_sentence("------")
good_sentence("GOOD")
good_sentence("------")

#   ____  ___   ___  ____  
#  / ___|/ _ \ / _ \|  _ \
# | |  _| | | | | | | | | |
# | |_| | |_| | |_| | |_| |
#  \____|\___/ \___/|____/

def bad_sentence(sentence:str):
    '''
    함수설명 :
        입력된 문자열을 pyfiglet형식으로 출력합니다.
        
    매개 변수 :
         sentence (str) : 출력할 문자열         
    '''
    py_sentence = pyfiglet.figlet_format(sentence)
    print(py_sentence)