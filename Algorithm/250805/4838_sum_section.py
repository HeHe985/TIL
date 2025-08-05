'''
데이터를 리스트로 저장한 후 M개의 요소의 합을 비교
최댓값/최솟값을 저장하는 변수와 현재 기준의 구간합을 계속 비교하여 갱신
'''

import sys
sys.stdin = open('4835.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 배열의 크기, M: 합을 계산할 구간의 크기
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_sum = 0
    min_sum = float('inf')
    # 리스트를 순회하며
    for i in range(0, N-M+1):
        sum_n = 0
        # i부터 M개의 값을 더하고
        for j in range(i, M+i):
            sum_n += arr[j]
        # max_n/min_n과 비교하여 값 갱신
        if max_sum < sum_n:
            max_sum = sum_n
        if min_sum > sum_n:
            min_sum = sum_n

    result = max_sum - min_sum

    print(f'#{tc} {result}')