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
    sound = '멍멍'
    # 생성자 메서드
    def __init__(self):
        super().__init__()
    # 클래스 메서드
    @classmethod
    def bark(cls):
        print(cls.sound)

class Cat(Animal):
    sound = '야옹'
    # 생성자 메서드
    def __init__(self):
        super().__init__()
    # 클래스 메서드
    @classmethod
    def meow(cls):
        print(cls.sound)

# class Pet(Dog, Cat):
class Pet(Cat, Dog):
    # 생성자 메서드
    def __init__(self):
        super().__init__()
    # 인스턴스 메서드
    def play(self):
        print('애완동물과 놀기')
    def make_sound(self):
        print(self.sound)
    # 매직 메서드
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'


pet1 = Pet()

print(pet1)