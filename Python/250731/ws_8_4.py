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

class Cat(Animal):
    # 생성자 메서드
    def __init__(self):
        super().__init__()
    # 스태틱 메서드
    @staticmethod
    def meow():
        print('야옹')

# cat1 = Cat()
# cat1.meow()
# dog1 = Dog()
# dog1.bark()


class Pet(Dog, Cat):
    # 생성자 메서드
    def __init__(self, sound):
        super().__init__()
        # 인스턴스 변수
        self.sound = sound
    # 인스턴스 메서드
    def play(self):
        print('애완동물과 놀기')
    def make_sound(self):
        print(self.sound)
    
pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
