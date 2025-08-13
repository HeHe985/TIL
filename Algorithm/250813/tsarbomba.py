import sys
sys.stdin = open('tsarbomba.txt')

# 상하좌우 델타 정의

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최대 폭발값을 저장할 변수
    max_bomb = 0
    # 행순회, 열순회
    for r in range(N):
        for c in range(M):
            # 현재 기준 값에서 폭할 할 수 있는 범위
            range_bomb = arr[r][c]
            # 폭발력을 누적으로 더해 저장할 변수
            sum_bomb = arr[r][c]
            # 상하좌우 네방향 순회
            for d in range(4):
                # 폭발 범위값을 1부터 순회하며
                for i in range(1, range_bomb + 1):
                    # 다음 좌표 계산
                    nx = r + dr[d] * i
                    ny = c + dc[d] * i
                    # 다음 좌표가 범위 안의 값이면 sum_bomb에 더함
                    if 0 <= nx < N and 0 <= ny < M:
                        sum_bomb += arr[nx][ny]
            # 최대값 갱신
            if max_bomb < sum_bomb:
                max_bomb = sum_bomb

    print(f'#{tc} {max_bomb}')