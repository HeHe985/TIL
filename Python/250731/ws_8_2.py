# 아래 클래스를 수정하시오.
class Animal:
    # 클래스 변수
    num_of_animal = 0
    # 생성자 메서드
    def __init__(self):
        Animal.increase_animal()
    # 클래스 메서드
    @classmethod
    def increase_animal(cls):
        cls.num_of_animal += 1

class Dog(Animal):
    # 생성자 메서드
    def __init__(self):
        super().__init__()
    # 스태틱 메서드
    @staticmethod
    def bark():
        print('멍멍!')


dog1 = Dog()
dog1.bark()
