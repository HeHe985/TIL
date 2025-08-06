'''
행과 열을 순환하며 최댓값을 저장하는 변수를 갱신
'''

import sys
sys.stdin = open('1209.txt')

T = 10
N = 100

# 행의 핪 중 최댓갔을 구하는 함수
def calculate_row_sum(data):
    r_max_val = 0
    for r in range(N):
        r_sum = 0
        for c in range(N):
            r_sum += data[r][c]
        if r_max_val < r_sum:
            r_max_val = r_sum
    return r_max_val

# 열의 핪 중 최댓갔을 구하는 함수
def calculate_col_sum(data):
    c_max_val = 0
    for c in range(N):
        c_sum = 0
        for r in range(N):
            c_sum += data[r][c]
        if c_max_val < c_sum:
            c_max_val = c_sum
    return c_max_val

# 대각선 핪 중 최댓갔을 구하는 함수
def calculate_dia_sum(data):
    d_max_val = 0
    d1_sum = 0
    d2_sum = 0
    for r in range(N):
        for c in range(N):
            if r == c:
                d1_sum += data[r][c]
            if abs(r - N + 1) == c:
                d2_sum += data[r][c]
    if d_max_val < d1_sum:
        d_max_val = d1_sum
    if d_max_val < d2_sum:
        d_max_val = d2_sum
    return d_max_val


for tc in range(1, T + 1):
    tc_n = int(input())
    max_val = 0
    # 100X100 배열
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    r_max = calculate_row_sum(arr)
    c_max = calculate_col_sum(arr)
    d_max = calculate_dia_sum(arr)


    print(f'#{tc_n} {max(r_max, c_max, d_max)}')