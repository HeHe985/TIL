import sys
sys.stdin = open('shark_elementary.txt')
# from heapq import heappush, heappop
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [[] for _ in range(N ** 2 + 1)]
    order = []
    # print(data)
    for _ in range(N ** 2):
        row = list(map(int, input().split()))
        data[row[0]] = row[1:]
        order.append(row[0])
    # data = [list(map(int, input().split())) for _ in range(N ** 2)]
    # print(data)
    position_map = [[0] * N for _ in range(N)]
    # 1. 비어있는 칸 중 인접칸에 좋아하는 학생이 가장 많은 칸
    # 2. 1만족이 여러개이면, 인접칸 중 비어있는 칸이 가장 많은 칸
    # 3. 2만족도 여러개이면, 행의 번호가 작은 칸, 열번호가 가장 작은 칸 순
    result = 0

    for student in order:
        possible_position = []
        for i in range(N):
            for j in range(N):
                if position_map[i][j] != 0:
                    continue
                empty = 0
                together = 0
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if position_map[nx][ny] == 0:
                            empty += 1
                        elif position_map[nx][ny] in data[student]:
                            together += 1
                # heappush(possible_position, (together, empty, i, j))
                possible_position.append((together, empty, i, j))
                # print(together)
        possible_position.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
        _, _, row, col = possible_position[0]
        # cnt_together, _, x, y = heappop(possible_position)
        # print('-----------------------')
        # print(row, col)
        position_map[row][col] = student

    # 만족도 계산
    for i in range(N):
        for j in range(N):
            student = position_map[i][j]
            cnt = 0
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if position_map[nx][ny] in data[student]:
                        cnt += 1

            if cnt != 0:
                result += 10 ** (cnt - 1)

    print(f'#{tc} {result}')



import sys
sys.stdin = open('shark_elementary.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
data = [[] for _ in range(N ** 2 + 1)]
order = []
for _ in range(N ** 2):
    row = list(map(int, input().split()))
    # 인덱스가 학생 번호이며, 선호학생을 저장한 data, 실제 배치 순서를 저장한 order
    data[row[0]] = row[1:]
    order.append(row[0])

# 좌석배치도
position_map = [[0] * N for _ in range(N)]
result = 0

# 입력 순서대로 학생 하나씩 검사 & 배치
for student in order:
    # 배치 가능한 좌석 리스트 초기화
    possible_position = []

    # 전체 행, 열 검사
    for i in range(N):
        for j in range(N):
            # 현재 자리가 이미 누가 배치되었다면 continue
            if position_map[i][j] != 0:
                continue
            empty = 0               # 현재 자리 기준 네방향 비어있는 자리 수
            together = 0            # 현재 자리 기준 네방향 선호 친구가 앉은 수

            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    # 인접한 자리에 아무도 없다면 empty +1
                    if position_map[nx][ny] == 0:
                        empty += 1
                    # 인접한 자리에 자신의 선호 친구가 있다면 together +1
                    elif position_map[nx][ny] in data[student]:
                        together += 1

            # 네방향 탐색 후 (인접한 선호 친구수, 인접한 빈자리수, 행, 열) 저장
            possible_position.append((together, empty, i, j))
    # 모든 자리 계산 후 아래의 조건에 따라 정렬
    # 1. 비어있는 칸 중 인접칸에 좋아하는 학생이 가장 많은 칸
    # 2. 1만족이 여러개이면, 인접칸 중 비어있는 칸이 가장 많은 칸
    # 3. 2만족도 여러개이면, 행의 번호가 작은 칸, 열번호가 가장 작은 칸 순
    possible_position.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    # 정렬된 리스트에서 가장 첫 요소의 좌표를 찾아 그 자리에 현재 탐색중인 학생 배치
    _, _, row, col = possible_position[0]
    position_map[row][col] = student

# 모든 배치 후 만족도 계산
for i in range(N):
    for j in range(N):
        student = position_map[i][j]
        cnt = 0
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if position_map[nx][ny] in data[student]:
                    cnt += 1

        if cnt != 0:
            result += 10 ** (cnt - 1)

print(result)