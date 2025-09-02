from collections import deque
import sys
sys.stdin = open('search_island.txt')

# 상하좌우 좌상 우상 우하 좌하 델타
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, 1, -1]


def bfs(arr):
    cnt = 0
    visited = [[False] * M for _ in range(N)]

    q = deque([(0, 0)])

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                continue
            while q:
                r, c = q.popleft()
                visited[r][c] = True

                for d in range(8):
                    nr, nc = r + dr[d], c + dc[d]

                    if (
                        0 <= nr < N
                        and 0 <= nc < M
                        and not visited[nr][nc]
                        and arr[nr][nc] == 1
                    ):

                        q.append((nr, nc))
            cnt += 1
    return cnt


N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
print(data)
result = bfs(data)
print(result)

