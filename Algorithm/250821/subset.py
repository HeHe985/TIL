

# 부분집합을 뽑는 함수
def comb(a, r):
    result = []
    if r == 0:
        return [[]]
    for i in range(len(a)):
        # i번 요소를 첫 요소로 뽑음
        elem = a[i]

        # 나머지에서 r-1개릐 조합을 재귀함수로 구현
        for rest in comb(a[i + 1:], r - 1):
            # 이미 선택한 요소 + 나머지를 합쳐 결과에 추가
            result.append([elem] + rest)

    return result


arr = [j for j in range(1, 11)]


# 부분 집합의 수
for n in range(1, len(arr) + 1):
    subset = comb(arr, n)
    # 각 부분집합의 합이 10이면 출력
    for k in subset:
        if sum(k) == 10:
            print(k)