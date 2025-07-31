# 아래 클래스를 수정하시오.
class Shape:
    # 생성자 메서드
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # 인스턴스 메서드
    # 가로 * 세로 값 반환
    def calculate_area(self):
        return self.width * self.height

shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)
