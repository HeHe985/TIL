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


class Cat(Animal):
    # 생성자 메서드
    def __init__(self):
        super().__init__()

class Pet(Dog, Cat):
    # 생성자 메서드
    def __init__(self):
        super().__init__()
    # 클래스 메서드
    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {Animal.num_of_animal}마리 입니다.'



dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())
