import sys
sys.stdin = open('guards.txt')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                for d in range(4):
                    for n in range(1, N + 1):
                        nx = i + dr[d] * n
                        ny = j + dc[d] * n
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                            arr[nx][ny] = 1
                        else:
                            break
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1

    print(f'#{tc} {cnt}')