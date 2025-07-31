# 아래 클래스를 수정하시오.
class Person:
    # 클래스 변수
    number_of_people = 0

    # 생성자 메서드
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 클래스 생성마다 해당 메서드 호출
        Person.increase_people()

    # 클래스 메서드
    # 클래스 변수 number_of_people 값을 1 증가
    @classmethod
    def increase_people(cls):
        cls.number_of_people += 1

    # 인스턴스 메서드
    # 자기소개 출력
    def introduce(self):
        print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')


person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people)
