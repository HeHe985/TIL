# 아래 클래스를 수정하시오.
class StringRepeater:
    # 생성자 메서드
    def __init__(self):
        pass

    # 스태틱 메서드
    # 반복 횟수와 문자열을 인자로 받아 문자열을 반복 출력
    @staticmethod
    def repeat_string(num, string):
        for i in range(num):
            print(string)

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
