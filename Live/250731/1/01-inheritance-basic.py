# 부모 클래스
class Animal:
    def eat(self):
        print('먹는 중')

# 자식 클래스
class Dog(Animal):
    def bark(self):
        print('멍멍')


my_dog = Dog()
my_dog.bark()

# 부모 클래스(Animal) 메서드 사용 가능
my_dog.eat()