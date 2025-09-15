import sys
sys.stdin = open('9490.txt')

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_flower = 0
    # 모든 좌표 검사
    for row in range(N):
        for col in range(M):
            # 자기 자신의 꽃가루 개수로 초기화
            flowers = arr[row][col]
            # 4방향 + 해당 칸의 값만큼 반복하며 검사
            for d in range(4):
                for i in range(1, arr[row][col] + 1):
                    nx, ny = row + dx[d] * i, col + dy[d] * i
                    if 0 <= nx < N and 0 <= ny < M:
                        flowers += arr[nx][ny]
            max_flower = max(max_flower, flowers)

    print(f'#{tc} {max_flower}')