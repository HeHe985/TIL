import sys
sys.stdin = open('2819.txt')

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move_n_connect(n, string, row, col):
    # 기저조건: 7자리 수를 만들면 완성된 문자열을 세트에 추가하고 탈출
    if n == 7:
        numbers.add(string)
        return
    # 현재 문자를 문자열 뒤에 붙임
    string += grid[row][col]
    # 네 방향 검사
    for d in range(4):
        nx, ny = row + dx[d], col + dy[d]
        # 범위 안이면 다음 재귀 호출
        if 0 <= nx < N and 0 <= ny < N:
            move_n_connect(n + 1, string, nx, ny)

T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    grid = [list(input().split()) for _ in range(4)]
    numbers = set()
    N = 4
    # 모든 칸 검사
    for i in range(N):
        for j in range(N):
            move_n_connect(0, '', i, j)

    print(f'#{tc} {len(numbers)}')