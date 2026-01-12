import pyfiglet
from termcolor import colored

# sentecte = "hellow"
# print(sentecte)
# # hellow

# py_sentecte = pyfiglet.figlet_format(sentecte)
# print(py_sentecte)

#  _          _ _
# | |__   ___| | | _____      __
# | '_ \ / _ \ | |/ _ \ \ /\ / /
# | | | |  __/ | | (_) \ V  V /
# |_| |_|\___|_|_|\___/ \_/\_/

# sentecte1 = pyfiglet.figlet_format("***")
# sentecte2 = pyfiglet.figlet_format("Hellow")
# sentecte3 = pyfiglet.figlet_format("~~~")
# print(sentecte1)
# print(sentecte2)
# print(sentecte3)

# __/\____/\____/\__
# \    /\    /\    /
# /_  _\/_  _\/_  _\
#   \/    \/    \/


#  _   _      _ _
# | | | | ___| | | _____      __
# | |_| |/ _ \ | |/ _ \ \ /\ / /
# |  _  |  __/ | | (_) \ V  V /
# |_| |_|\___|_|_|\___/ \_/\_/


#  /\//\//\/|
# |/\//\//\/

# sentecte4 = pyfiglet.figlet_format("@@@")
# sentecte5 = pyfiglet.figlet_format("###")
# sentecte6 = pyfiglet.figlet_format("&&&")
# sentecte7 = pyfiglet.figlet_format("^^^")
# print(sentecte4)
# print(sentecte5)
# print(sentecte6)
# print(sentecte7)

#   ____    ____    ____  
#   / __ \  / __ \  / __ \
#  / / _` |/ / _` |/ / _` |
# | | (_| | | (_| | | (_| |
#  \ \__,_|\ \__,_|\ \__,_|
#   \____/  \____/  \____/

#    _  _     _  _     _  _
#  _| || |_ _| || |_ _| || |_
# |_  ..  _|_  ..  _|_  ..  _|
# |_      _|_      _|_      _|
#   |_||_|   |_||_|   |_||_|


#   ___    ___    ___
#  ( _ )  ( _ )  ( _ )
#  / _ \/\/ _ \/\/ _ \/\
# | (_>  < (_>  < (_>  <
#  \___/\/\___/\/\___/\/


#  /\ /\ /\
# |/\|/\|/\|

# text = pyfiglet.figlet_format("PTU Python", font="slant")
# print(text)
# #     ____  ________  __   ____        __  __
#    / __ \/_  __/ / / /  / __ \__  __/ /_/ /_  ____  ____
#   / /_/ / / / / / / /  / /_/ / / / / __/ __ \/ __ \/ __ \
#  / ____/ / / / /_/ /  / ____/ /_/ / /_/ / / / /_/ / / / /
# /_/     /_/  \____/  /_/    \__, /\__/_/ /_/\____/_/ /_/
#                            /____/

# 글자 생성 후 초록색(green) 적용
# ascii_art = pyfiglet.figlet_format("SUCCESS")
# colored_ascii = colored(ascii_art, 'green')

# print(colored_ascii)

# / ___|| | | |/ ___/ ___| ____/ ___/ ___|
# \___ \| | | | |  | |   |  _| \___ \___ \
#  ___) | |_| | |__| |___| |___ ___) |__) |
# |____/ \___/ \____\____|_____|____/____/

# my_words = ["Start", "Process", "Finish"]

# for word in my_words:
#     print(f"--- {word} 단계를 출력합니다 ---")
#     art = pyfiglet.figlet_format(word, font="digital")
#     print(art)
   
#     --- Start 단계를 출력합니다 ---
# +-+-+-+-+-+
# |S|t|a|r|t|
# +-+-+-+-+-+

# --- Process 단계를 출력합니다 ---
# +-+-+-+-+-+-+-+
# |P|r|o|c|e|s|s|
# +-+-+-+-+-+-+-+

# --- Finish 단계를 출력합니다 ---
# +-+-+-+-+-+-+
# |F|i|n|i|s|h|
# +-+-+-+-+-+-+ 

# print(pyfiglet.FigletFont.getFonts()) # 사용 가능한 모든 폰트 리스트 출력