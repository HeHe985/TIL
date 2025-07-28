def find_min_max(lst):
    # return min(lst), max(lst)
    '''
    주어진 리스트에서 최소와 최대값을 찾아 튜플로 반환하는 함수
    '''
    # 최소와 최대 값의 기준이 될 변수 지정
    # 주어진 리스트의 첫번째 요소를 기준으로 지정
    min_val = lst[0]
    max_val = lst[0]

    # 리스트의 두번째 요소부터 순회 시작
    for num in lst[1:]:
        
        # 최솟값 갱신
        # 만약에 현재 순회 번호인 num가 최소 기준 값이 min_val보다 작으면,
        # 기존 min_val를 num으로 갱신(업데이트)
        if num < min_val:
            min_val = num

        # 최댓값 갱신
        # 만약에 현재 순회 번호인 num가 최eo 기준 값이 max_val보다 크면,
        # 기존 max_val를 num으로 갱신(업데이트)
        if num > max_val:
            max_val = num

    # 반복이 종료되면, 자연스럽게 min_val, max_val가 완성되어있음
    return min_val, max_val


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
