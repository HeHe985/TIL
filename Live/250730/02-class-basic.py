class Person:
    # 생성자 메서드
    def __init__(self, name, age):  # 인스턴스를 만들떄 호출됨
        # 인스턴스 속성
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')
