import sys
from heapq import heappush, heappop
sys.stdin = open('1249.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra(x, y):
    pq = [(0, x, y)]
    times = [[float('inf')] * N for _ in range(N)]

    times[x][y] = 0
    # pq가 빌 때까지 하나씩 꺼내서 검사
    while pq:
        current_time, current_x, current_y = heappop(pq)
        # 현재 꺼낸 값의 좌표 기준
        # 이미 더 작은 시간으로 갱신한 적이 있으면 패스
        if times[current_x][current_y] < current_time:
            continue

        # 네방향 탐색
        for d in range(4):
            nx, ny = current_x + dx[d], current_y + dy[d]
            if not(0 <= nx < N and 0 <= ny < N):
                continue
            new_time = current_time + map_info[nx][ny]
            # 다음 좌표가 이미 더 작거나 같은 시간으로 갱신한 적이 있으면 패스
            if times[nx][ny] <= new_time:
                continue
            # 위의 경우가 모두 아니라면 시간을 갱신하고 핍푸시
            times[nx][ny] = new_time
            heappush(pq, (new_time, nx, ny))

    # 다익스트라 종료후
    return times[N - 1][N - 1]


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    map_info = [list(map(int, input())) for _ in range(N)]

    result = dijkstra(0, 0)

    print(f'#{tc} {result}')