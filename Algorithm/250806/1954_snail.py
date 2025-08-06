'''
방향을 전환할 때 마다 그 방향으로 갈수 있는 거리값이 줄어듦?
우- 하- 좌- 상 순으로 반복
범위를 넘거나, 이미 값이 채워져 있다면 방향을 바꾼다!
'''

import sys
sys.stdin = open('1954.txt')

T = int(input())

# 우하좌상 델타
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    # 현재 위치
    r_now = 0
    c_now = 0
    # 달팽이 숫자를 저장할 비어있는 배열
    snail = [[0] * N for _ in range(N)]
    # 방향 인덱스
    dir = 0
    i = 0
    while i <= N * N:
        snail[r_now][c_now] = i
        next_r = r_now + dr[dir]
        next_c = c_now + dc[dir]
        if 0 <= next_r < N and 0 <= next_c < N and snail[next_r][next_c] == 0:
            r_now = next_r
            c_now = next_c
            i += 1
        else:
            dir += 1


    print(f'#{tc} {snail}')