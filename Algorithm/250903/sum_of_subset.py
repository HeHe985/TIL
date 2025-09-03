# itertools 미사용
import sys
sys.stdin = open('sum_of_subset.txt')


# 부분집합의 합이 0이 되는 지 확인하는 함수
def is_zero_subset(a):
    for i in range(1, 1 << N):
        sum_of_subset = 0
        for j in range(N):
            # i의 j번째가 1이라면
            if i & (1 << j):
                sum_of_subset += a[j]
        if sum_of_subset == 0:
            return 1
    else:
        return 0


T = int(input())
N = 10

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    result = is_zero_subset(arr)
    print(f'#{tc} {result}')




# itertools 사용
'''
import itertools
import sys
sys.stdin = open('sum_of_subset.txt')

T = int(input())
for tc in range(1, T + 1):
    N = 10
    arr = list(map(int, input().split()))
    result = 0
    
    for n in range(1, N + 1):
        subsets = itertools.combinations(arr, n)
        for subset in subsets:
            sum_subset = sum(subset)
            if sum_subset == 0:
                result = 1

    print(f'#{tc} {result}')
'''