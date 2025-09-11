import sys
sys.stdin = open('1861.txt')

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 이동할 수 없을 때 까지 무한 이동~~
def move_to(row, col):
    # 이미 검사했던 좌표에 속하면 더이상 검사 안함
    if visited[row][col]:
        return visited[row][col]
    visited[row][col] = 1

    # 네방향 다 한번씩 이동해 봄
    for d in range(4):
        nx, ny = row + dx[d], col + dy[d]
        # 1. 범위 안이 아닐 때
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        # 2. 현재 방의 숫자 보다 1큰 경우가 아닐때
        if not (A[nx][ny] == A[row][col] + 1):
            continue
        # 해당 칸에서 출발할 때 가장 많이 방을 들리고 가는 수를 찾기 위함
        visited[row][col] = max(visited[row][col], move_to(nx, ny) + 1)

    return visited[row][col]


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    max_cnt = 0
    start_room = N * N
    # 모든 칸에서 출발해봄
    for i in range(N):
        for j in range(N):
            cnt = move_to(i, j)
            if max_cnt < cnt:
                max_cnt = cnt
                start_room = A[i][j]
            elif max_cnt == cnt:
                start_room = min(start_room, A[i][j])

    print(f'#{tc} {start_room} {max_cnt}')