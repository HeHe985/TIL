# 아래 클래스를 수정하시오.
class Shape:
    # 생성자 메서드
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # 인스턴스 메서드
    # 사각형 정보 출력    
    def print_info(self):
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        print(f'Area: {self.width * self.height}')
        print(f'Perimeter: {(self.width + self.height) * 2}')

shape1 = Shape(5, 3)
shape1.print_info()
