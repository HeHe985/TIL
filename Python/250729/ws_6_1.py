# 아래 함수를 수정하시오.
def union_sets(set_1, set_2):
    '''두개의 set을 인자로 받아 합집합 반환'''
    return set_1.union(set_2)

def union_multiple_sets(*sets):
    # 두개 이상의 set을 넘겨 받았는 지 검사 후
    if len(sets) < 2:
        print('최소 두개의 셋이 필요합니다.')
    # 모든 set을 순회하며 합집합 진행
    else:
        final_set = set()
        for s in sets:
            final_set = final_set | s
        return final_set


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
# 출력 : 최소 두 개의 셋이 필요합니다
