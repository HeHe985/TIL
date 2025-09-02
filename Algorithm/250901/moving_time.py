from collections import deque
import sys
sys.stdin = open('moving_time.txt')

# 상하좌우 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(N, M):
    # -1: 미방문
    distance = [[-1] * M for _ in range(N)]

    # 처음 시작 위치
    q = deque([(0, 0)])
    distance[0][0] = 0

    # 큐가 빌 때까지
    while q:
        # 큐의 첫 요소를 하나 꺼냄
        r, c = q.popleft()

        # 목적지에 도착했을 경우 현재 위치에서의 거리 반환
        if r == N - 1 and c == M - 1:
            return distance[r][c]

        # 네 방향 탐색
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]


            if (
                # 다음 이동할 위치가 범위 안이고
                0 <= nr < N
                and 0 <= nc < M
                # 이동할 수 있는 길이고
                and data[nr][nc] == 1
                # 방문한 적 없을 경우
                and distance[nr][nc] == -1
            ):
                # 거리를 이동 전 거리에서 +1하고 큐에 추가
                distance[nr][nc] = distance[r][c] + 1
                q.append((nr, nc))
    # 큐가 빌 때까지 반복을 완료하고 빠져 나왔는데 반환값이 없다면 목적지까지 가는 경로가 없음
    return -1


N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]

result = bfs(N, M)
print(result)