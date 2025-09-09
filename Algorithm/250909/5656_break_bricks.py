from collections import deque
import sys
sys.stdin = open('5656.txt')

'''
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1
'''
'''
N: 구슬 던지기 횟수
W: 열
H: 헹
'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 구슬을 던져 벽돌을 깨고 남은 최소 벽돌 수를 찾는 함수
def shoot(cnt, remains, arr):
    global min_bricks
    # 구슬을 다 던졌거나 남아있는 벽돌이 없으면 그만
    if cnt == N or remains == 0:
        min_bricks = min(min_bricks, remains)
        return
    # 모든 열에서 한번씩 던져봄
    for col in range(W):
        # 현재 벽돌의 상태를 나타내는 배열
        now_arr = [row[:] for row in arr]

        # 현재 열에서 가장 위에 있는 벽돌 찾기
        top = -1
        for row in range(H):
            if now_arr[row][col]:
                top = row
                break
        # 해당 열에 벽돌이 아예 없다면 넘어감
        if top == -1:
            continue

        # 큐 초기화. 첫 후보군 삽입(행번호, 열번호, 해당 좌표의 값)
        q = deque([(top, col, now_arr[top][col])])
        # 현재 맞힌 벽돌을 깨고(=0) 남은 벽돌 수에서 -1
        now_arr[top][col] = 0
        now_remains = remains - 1

        # 큐가 빌때까지 하나씩 꺼내서 검사
        while q:
            x, y, val = q.popleft()

            for i in range(val):
                for d in range(4):
                    nx, ny = x + dx[d] * i, y + dy[d] * i
                    # 범위 안이 아니면 검사 안함
                    if not(0 <= nx < H and 0 <= ny < W):
                        continue
                    # 벽돌이 없다면 검사 안함
                    if now_arr[nx][ny] == 0:
                        continue

                    # 큐에 추가하여 다음 검사할 후보로 추가
                    q.append((nx, ny, now_arr[nx][ny]))
                    # 벽돌을 깨고(=0), 남은 벽돌 수 -1
                    now_arr[nx][ny] = 0
                    now_remains -= 1

        # 벽돌 위치 재정비
        # 1열씩 검사
        for c in range(W):
            idx = H - 1
            # 해당 열의 맨 아래 벽돌부터 검사
            for r in range(H - 1, -1, -1):
                if now_arr[r][c]:
                    now_arr[r][c], now_arr[idx][c] = now_arr[idx][c], now_arr[r][c]
                    idx -= 1

        # 재귀 호출로 구슬 또 던짐
        shoot(cnt + 1, now_remains, now_arr)


T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    min_bricks = H * W

    # 현재 벽돌 수 구하기
    num_bricks = 0
    for i in range(H):
        for j in range(W):
            if bricks[i][j]:
                num_bricks += 1

    shoot(0, num_bricks, bricks)

    print(f'#{tc} {min_bricks}')