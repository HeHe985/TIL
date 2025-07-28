# 아래 함수를 수정하시오.

# 최솟값/최댓값 찾기
def find_min_max(original_list):
    '''
    인자로 받은 리스트를 오름차순 정렬 후 처음 요소와 마지막 요소를 튜플로 반환
    '''
    original_list.sort()
    minimum = original_list.pop(0)
    maximum = original_list.pop()
    return (minimum, maximum)


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
