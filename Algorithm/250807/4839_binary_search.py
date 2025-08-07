'''

'''
import sys
sys.stdin = open('4839.txt')

T = int(input())

# 이진 탐색
def binary_search(k, n):
    start = 1
    end = n
    cnt = 0
    while start + 1 <= end:
        middle = int((start + end) / 2)
        cnt += 1
        if middle == k:
            return cnt
        elif middle > k:
            end = middle
        else:
            start = middle
    return 1000

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    cnt_A = binary_search(A, P)
    cnt_B = binary_search(B, P)
    if cnt_A < cnt_B:
        result = 'A'
    elif cnt_A > cnt_B:
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')