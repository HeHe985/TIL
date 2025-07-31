# 아래 클래스를 수정하시오.
class Shape:
    # 생성자 메서드
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 인스턴스 메서드
    # 사각형의 둘레 계산 후 반환
    def calculate_perimeter(self):
        return (self.width + self.height) * 2

shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)
