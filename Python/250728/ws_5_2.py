# 아래 함수를 수정하시오.

# 중복 요소를 제거해 새로운 리스트를 반환하는 함수
def remove_duplicates(duplicate_list):
    '''
    for 문을 사용해 인자로 받은 리스트를 순회하며,
    초기에 비어있던 new_lst에 존재하지 않는 값만 추가한다.
    '''
    new_lst = []
    for i in duplicate_list:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst

    '''
    # set을 이용해 중복을 제거하고 다시 리스트로 형변환하는 방법도 있다.
    new_lst = list(set(duplicate_list))
    return new_lst
    '''

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
