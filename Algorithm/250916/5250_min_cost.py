import sys
sys.stdin = open('5250.txt')
from heapq import heappush, heappop

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra(start_x, start_y):
    # 최소 비용 저장할 배열
    cost = [[float('inf')] * N for _ in range(N)]
    pq = []

    # 초기값 저장 및 힙에 삽입
    cost[start_x][start_y] = 0
    heappush(pq, (0, start_x, start_y))

    # 큐가 빌때까지 하나씩 힙팝!
    while pq:
        current_cost, current_x, current_y = heappop(pq)
        # 이미 더 적은 비용으로 간적이 있다면 패스
        if cost[current_x][current_y] < current_cost:
            continue

        # 네방향을 순회하며
        for d in range(4):
            nx, ny = current_x + dx[d], current_y + dy[d]
            # 범위 밖이면 패스
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            # 다음 좌표의 높이가 더크면
            if heights[current_x][current_y] < heights[nx][ny]:
                new_cost = current_cost + heights[nx][ny] - heights[current_x][current_y] + 1
            # 작거나 같으면
            else:
                new_cost = current_cost + 1

            # 새로 계산한 비용보다 더 적은 비용으로 방문한 적이 없다면
            if cost[nx][ny] > new_cost:
                # 값을 갱신하고 힙에 삽입
                cost[nx][ny] = new_cost
                heappush(pq, (new_cost, nx, ny))

    return cost


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]

    result_arr = dijkstra(0, 0)

    print(f'#{tc} {result_arr[N - 1][N - 1]}')

