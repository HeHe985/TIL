# 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
negative = -3
print(abs(negative))

# 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
empty_list = []
print(bool(empty_list))

# 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
my_list = [1, 2, 3, 4, 5]
print(sum(my_list))

# 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
unsorted_list = ['하', '교', '캅', '의', '지', '가']
print(sorted(unsorted_list))


def create_user(name, age, address):
    user_info = {'name': name, 'age': age, 'address': address}
    print(f'{name}님 환영합니다!')

    return user_info

user_data = [('김시습', 20, '서울'), ('허균', 16, '강릉'), ('남영로', 52, '조선'), ('임제', 36, '나주'), ('박지원', 60, '한성부')]


print(list(map(lambda args: create_user(*args),user_data)))