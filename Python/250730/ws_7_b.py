# 아래에 코드를 작성하시오.

class Myth:
    # 클래스 변수
    type_of_myth = 0

    # 생성자 메서드
    def __init__(self, name):
        self.name = name
        # 인스턴스 생성마다 클래스 메서드 호출
        Myth.increase_myth()
    
    # 클래스 메서드
    @classmethod
    def increase_myth(cls):
        cls.type_of_myth += 1
    
    # 스태틱 메서드
    # 신화에 대한 설명 출력
    @staticmethod
    def description():
        print('신화는 한 나라 혹은 한 민족으로 부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')

# 인스턴스 생성
m1 = Myth('dangun')
m2 = Myth('greek & rome')

# 각 인스턴스의 name 출력
print(m1.name)
print(m2.name)

print(f'현재까지 생성된 신화 수 : {Myth.type_of_myth}')
Myth.description()