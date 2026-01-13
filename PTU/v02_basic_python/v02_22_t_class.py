# 클래스 실습 예제
#  조건 :
#  1) 생성자 파라미터 self 제외 4개
#  2) 매세드 총 2개 이상
#  3) 객체 3개 생성

# class Customer:
#     def __init__(self, name, age, gender, phone_number):
#         # 속성
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.phone_number = phone_number
        
#     def list(self):
#         print(f" 손님의 성명은 {self.name}입니다. 나이는 {self.age}세이고 {self.gender}이며, 전화번호는 {self.phone_number}입니다.")
    
#     def worker(self):
#         print(f" 직원의 성명은 {self.name}입니다. 나이는 {self.age}세이고 {self.gender}이며, 전화번호는 {self.phone_number}입니다.")
    
        
# # 객체생성
# cs1 = Customer("김철수", "30", "남성", "010-000-0000")
# cs2 = Customer("김영희", "17", "여성", "010-000-0000")
# cs3 = Customer("박철수", "20", "남성", "010-000-0000")


# # 메서드 호출
# cs1.list()
# cs2.list()
# cs3.list()
# cs1.worker()
# cs2.worker()
# cs3.worker()

#  클래스 정의
class Car:
    '''
    차량에 대한 클래스
    '''
    # 생성자
    def __init__(self, name, brand, year, color):
        #  속성
        self.name = name
        self.brand = brand
        self.year = year
        self.color = color
        
    # 메서드 1 : 자동차 정보 출력
    def info(self):
        print(f"차량명 : {self.name}, 브랜드 : {self.brand}, 연식 : {self.year}, 색상 : {self.color}")

    # 메서드 2 : 자동차 운전
    def drive(self):
        print(f"{self.name} 달립니다.!!")
        
# 객체 생성
car1 = Car("쏘나타", "현대", "2026", "화이트")
car2 = Car("모델S", "테슬라", "2025", "블랙")
car3 = Car("911", "포르쉐", "2020", "레드")

# 메서드 호출
car1.info() # 차량명 : 쏘나타, 브랜드 : 현대, 연식 : 2026, 색상 : 화이트
car1.drive() # 쏘나타 달립니다.!!
car3.info() # 차량명 : 911, 브랜드 : 포르쉐, 연식 : 2020, 색상 : 레드
car3.drive() # 911 달립니다.!!

# # 모든 사람의 공통 설계를 담은 부모 클래스
# class Person:
#     def __init__(self, name, age, sex, phone_number):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.phone_number = phone_number

#     def show_info(self):
#         print(f" 성명: {self.name}, 나이: {self.age}세, 성별: {self.sex}, 연락처: {self.phone_number}")

# # Person을 상속받은 손님 클래스
# class Customer(Person):
#     def show_info(self):
#         print("[손님 정보]", end="")
#         super().show_info() # 부모 클래스의 show_info를 가져와서 씁니다.

# # Person을 상속받은 직원 클래스
# class Worker(Person):
#     def show_info(self):
#         print("[직원 정보]", end="")
#         super().show_info()

# # 객체 생성
# cs1 = Customer("김철수", 30, "남성", "010-111-1111")
# wk1 = Worker("박매니저", 45, "여성", "010-222-2222")

# # 메서드 호출
# cs1.show_info()
# wk1.show_info()
            
            