import termcolor
from termcolor import colored

# colored(출력할 문장렬, 글자색, 배경색, atts=[스타일])
 
color_sentence = colored(
    "Hello",
    "red",
    "on_green",
    ["bold", "reverse"]
)
print(color_sentence)
    

