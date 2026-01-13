#  Animal 클래스

#  클리스 정의
class Animal:
    # 생성자
    def __init__(self, name, age):
        #  속성
        self.name = name
        self.age = age
        
    def hello(self):
        print(f"안녕하세요. 저는 {self.name}입니다. 그리고 {self.age}살 입니다.")
    
# 객체 생성
dog = Animal("뽀삐", 99)

# 메서드 호출
dog.hello()

# 객체 생성2
cat = Animal("냥이", 100)
cat.hello()