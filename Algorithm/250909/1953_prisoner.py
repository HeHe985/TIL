import sys
from collections import deque
sys.stdin = open('1953.txt')

'''
N: 지하 터널 지도의 세로크기
M: 지하 터널 지도의 가로 크기
R: 맨홀 뚜껑의 세로 위치
C: 맨홀 뚜껑의 가로 위치
L: 탈출 후 소요 시간
data: 지하 터널 지도 정보(0: 터널 없음)
'''
# 상하좌우 델타
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 터널 방향
types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}


# 터널 탐색 BFS 함수
def bfs():
    q = deque()
    q.append((R, C))
    visited[R][C] = 1

    # 큐가 빌 때 까지
    while q:
        x, y = q.popleft()
        direction = types[map_info[x][y]]

        # 네 방향 탐색
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            # 다음 반복으로 넘어가는 경우
            # 1. 현재 터널이 못가는 방향 일 때
            if direction[d] == 0:
                continue
            # 2. 범위안의 값이 아닐 때
            if not(0 <= nx < N and 0 <= ny < M):
                continue
            # 3. 이미 방문한 칸일 때
            if visited[nx][ny] > 0:
                continue
            # 4. 해당 좌표의 지도 정보가 0일때
            if map_info[nx][ny] == 0:
                continue
            # 5. 길이가 L이상 일 때
            if visited[x][y] >= L:
                continue

            next_direction = types[map_info[nx][ny]]

            # 6. 현재와 다음 터널이 연결이 안될 때
            # 현재가 상 or 좌(0 or 2)인데 다음이 하 / 우(1, 3)가 아닌 경우
            if d % 2 == 0 and next_direction[d + 1] == 0:
                continue
            # 현재가 하 or 우(1 or 3)인데 다음이 상 / 좌(0, 2)가 아닌 경우
            if d % 2 == 1 and next_direction[d - 1] == 0:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1


T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    map_info = [list(map(int, input().split())) for _ in range(N)]

    # 방문 체크와 동시에 걸린 시간을 기록
    visited = [[0] * M for _ in range(N)]

    bfs()
    cnt = 0
    # 개수 세기
    for i in range(N):
        for j in range(M):
            if visited[i][j] > 0:
                cnt += 1

    print(f'#{tc} {cnt}')





'''
# 터널 방향
types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}

def bfs(R, C):

    q = deque([(R, C)])
    # 출발점 초기화
    visited[R][C] = 1

    # 큐가 빌 때까지
    while q:
        x, y = q.popleft()
        directions = types[data[x][y]]

        for d in range(4):
            # 갈 곳이 없을 경우
            if directions[d] == 0:
                continue
            # L시간 이후는 넘어감
            if visited[x][y] >= L:
                continue

            nx, ny = x + dx[d], y + dy[d]

            if not(0 <= nx < N and 0 <= ny < M):
                continue
            if data[nx][ny] == 0:
                continue
            if visited[nx][ny]:
                continue

            next_directions = types[data[nx][ny]]

            # 현재 상좌 -> 다음이 하우
            if d % 2 == 0 and next_directions[d + 1] == 0:
                continue
            # 현재 하우 -> 다음이 상좌
            if d % 2 == 1 and next_directions[d - 1] == 0:
                continue


            # 시간을 +1 해주면서 기록
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 특정 좌표까지 걸린 시간을 기옥
    visited = [[0] * M for _ in range(N)]
    bfs(R, C)
    cnt = 0

    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'#{tc} {cnt}')
'''