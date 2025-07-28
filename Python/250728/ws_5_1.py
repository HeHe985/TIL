# 아래 함수를 수정하시오.

# 문자열을 역순으로 반환하는 함수
def reverse_string(reverse_string):
    '''
    문자열을 받아 내장함수 reversed를 사용한다.
    그 결과 역순으로 정렬된 이터레이터가 나오기 때문에 join을 이용하여 문자열 형태로 연결해준다.
    '''
    return(''.join(reversed(reverse_string)))

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
