# 아래 클래스를 수정하시오.
class Shape:
    # 생성자 메서드
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # 매직 메서드
    # 인스턴스를 문자열로 표현
    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'

shape1 = Shape(5, 3)
print(shape1)