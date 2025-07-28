# 아래 함수를 수정하시오.

# 오름차순 정렬
def sort_tuple(sort_tuple):
    '''
    내장함수 sorted를 이용하여 오름차순 정렬한 튜플 반환
    '''
    new_tuple = ()
    new_tuple = sorted(sort_tuple)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
