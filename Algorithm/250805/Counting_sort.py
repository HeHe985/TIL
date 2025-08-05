# Counting 정렬

'''
데이터 리스트를 순회하며 빈도수를 저장
빈도수를 누적합으로 변경
데이터 리스트의 마지막부터 역으로 순회하며
빈도수를 저장한 리스트를 참고하여 결과 리스트에 저장
'''

# input data
a = [0, 4, 1, 3, 1, 2, 4, 1]

# 빈도수를 저장할 리스트(0~5)
counts = [0] * 5
# 정렬된 리스트 초기화
result = [0] * len(a)
# a를 순회하며 빈도수 저장
for i in a:
    counts[i] += 1
print(counts)
# 빈도수 리스트를 누적합으로 변경
for j in range(1, 5):
    counts[j] += counts[j - 1]
print(counts)

# a를 역으로 순회
for k in range(len(a)-1, -1, -1):
    # counts 에서 해당 값 -1
    counts[a[k]] -= 1
    # counts에 저장되어 있는 값번째에 저장
    result[counts[a[k]]] = a[k]

print(result)