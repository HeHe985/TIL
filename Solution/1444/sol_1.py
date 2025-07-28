def even_elements(lst):
    '''
    이 함수는 원본 리스트를 순회하면서
    짝수만 찾아서 새로운 리스트를 만들고 반환
    '''
    # 짝수만 담을 빈 리스트 생성
    result = []
    # while
    # 원본 리스트가 빌 때까지 반복
    while len(lst) > 0:
        # 리스트의 첫번째 요소를 제거하면서 따로 담기
        element = lst.pop(0)
        # 제거한 요소가 짝수인지 확인
        if element % 2 == 0:
            # 짝수면 새로운 리스트에 추가
            result.extend([element])
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
