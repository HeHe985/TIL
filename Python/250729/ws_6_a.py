my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.

# my_set을 순회하며 얻은 값을 key로하는 my_dict 값 출력
for element in my_set:
    print(my_dict.get(element))

# var에 튜플 할당
var = (1, 2, 3, 'A')
# my_dict에 var 튜플 추가
my_dict.update({var: '변수로도 키 설정 가능'})

print(my_dict)