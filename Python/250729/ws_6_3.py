# 아래 함수를 수정하시오.
# 두개의 셋을 인자로 받아 교집합 반환
def intersection_sets(set1, set2):
    sets = set1.intersection(set2)
    # sets = set1 & set2
    # 교집합이 없을 경우 메시지 출력
    if len(sets) == 0:
        print('공통 요소가 없습니다.')
    
    return len(sets), sets

result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)  # (1, {3})

result = intersection_sets({1, 2}, {3, 4})
print(result)  # (0, set())
# 출력: 공통 요소가 없습니다
