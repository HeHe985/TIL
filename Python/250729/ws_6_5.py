# 두 셋을 인자로 받아 차집합을 반환
def ordered_difference_sets(set1, set2):
    # 각 방향의 차집합을 각각 할당
    result1 = set1 - set2
    result2 = set2 - set1
    # 첫번째 차집합의 길이가 더 짧거나 같을때 
    if len(result1) <= len(result2):
        return result1, result2
    # 두번째 차집합의 길이가 더 짧을 때
    else:
        return result2, result1

# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})
