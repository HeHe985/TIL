'''
짝수번째 N-1, N-2,  N-3, ..., N // 2
홀수번째 0, 1, 2, 3, ..., (N // 2) - 1

오름차순 정렬
돌아가면서 하나씩 뽑음
'''

import sys
sys.stdin = open('4843.txt')

# 오름차순 정렬
def sort_asc(arr):
    for i in range(N - 1):
        min_i = i
        for j in range(i + 1, N):
            if arr[min_i] > arr[j]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = sort_asc(arr)
    result = []
    for n in range(10):
        # 짝수 인덱스에서는 뒤에서 pop
        if n % 2 == 0:
            result.append(sorted_arr.pop())
        # 홀수 인덱스에서는 앞에서 pop
        else:
            result.append(sorted_arr.pop(0))

    print(f'#{tc} {" ".join(map(str, result))}')

