import sys
sys.stdin = open('subset.txt')

T = int(input())
N = 10

# 부분집합의 합이 0이 되는지 구하는 함수
def calculate_subset(a, n):
    # 공집합 제외
    for i in range(1, 1 << n):
        sum_of_subset = 0
        for j in range(n):
            # i의 j번째가 1이라면
            if i & (1 << j):
                # 부분집합의 합 변수에 더함
                sum_of_subset += a[j]
        if sum_of_subset == 0:
            return 1
    else:
        return 0

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    result = calculate_subset(arr, N)

    print(f'#{tc} {result}')