def even_elements(lst):
    # 리스트의 길이만큼 반복
    for _ in range(len(lst)):
        # 리스트의 첫번째 요소를 꺼냄
        num = lst.pop(0)
        # 꺼낸 요소가 짝수인지 확인
        if num % 2 == 0:
            # 짝수면 리스트의 맨 뒤에 다시 추가
            lst.extend([num])
    # 홀수는 버려지고 짝수만 남은 리스트가 남게 됨
    return lst

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
