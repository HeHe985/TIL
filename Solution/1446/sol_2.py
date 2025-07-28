def find_min_max(lst):
    '''
    이 함수는 인자로 받은 리스트를 오름차순으로 정렬한 후,
    첫번째와 마지막 요소를 반환하는 함수
    '''

    # 원본 리스트를 변경하지 않기 위해 복사본 지정
    sorted_lst = lst[:]

    # 리스트의 길이만큼 반복
    for idx in range(len(sorted_lst)):
        # 현재 인덱스를 최솟값의 인덱스로 가정
        min_index = idx
        # idx 뒤에 있는 나머지 원소들과 비교하기 위해 나머지 원소들을 순회
        for j in range(idx + 1, len(sorted_lst)):
            # j에서 더 작은 원소를 찾으면, 최솟값의 인덱스를 갱신(업데이트)
            if sorted_lst[min_index] > sorted_lst[j]:
                min_index = j
        # [1, 3, 7, 2, 5], [1, 2, 7, 3, 5], ...
        # min_idx 0 >>> 1
        # 이 작은 for문이 끝나면 최소 인덱스가 나왔기 때문에
        # 현재 위치(idx)의 요소와 새로 찾은 최소 인덱스 위치의 요소 위치를 바꿈(swap)
        sorted_lst[idx], sorted_lst[min_index] = sorted_lst[min_index], sorted_lst[idx]
        # print(sorted_lst)
    min_val = sorted_lst[0]
    max_val = sorted_lst[-1]
    return min_val, max_val

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
