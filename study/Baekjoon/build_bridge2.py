import sys
sys.stdin = open('build_bridge2.txt')
from collections import deque
'''
0: 바다
1: 땅
'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_island():
    checked = [[False] * M for _ in range(N)]
    islands = []
    for i in range(N):
        for j in range(M):
            if map_info[i][j] == 0:
                continue
            if checked[i][j]:
                continue
            islands.append((i, j))
            q = deque()
            q.append((i, j))
            checked[i][j] = True

            while q:
                now_x, now_y = q.popleft()
                for d in (1, 3):
                    nx, ny = now_x + dx[d], now_y + dy[d]
                    if not (0 <= nx < N and 0 <= ny < M):
                        continue
                    if map_info[nx][ny] == 0:
                        continue
                    if checked[nx][ny]:
                        continue
                    q.append((nx, ny))
                    checked[nx][ny] = True

    return islands


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    map_info = [list(map(int, input().split())) for _ in range(N)]

    start_points = find_island()
    print(start_points)

    # print(result)