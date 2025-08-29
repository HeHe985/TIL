import sys
sys.stdin = open('4875.txt')


def dfs(i, j):
    # 상하좌우 델타
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 먼저 방문했다고 표시
    visited[i][j] = True

    # 네방향 검사
    for d in range(4):
        nr, nc = i + dr[d], j + dc[d]

        # 미로 범위 안이고,
        if 0 <= nr < N and 0 <= nc < N:
            # 다음 방문할 곳이 출구일 경우 1리턴
            if arr[nr][nc] == 2:
                return 1
            # 방문한적 없으며, 벽이 아닐시
            elif not visited[nr][nc] and arr[nr][nc] == 0:
                # 재귀 함수 호출과 동시에 리턴값을 중간 저장
                mid_return = dfs(nr, nc)
                # 재귀를 마치고 온 함수의 반환값이 1이면 리턴 1
                if mid_return == 1:
                    return 1

    return 0


T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)

    # 방문여부
    visited = [[False] * N for _ in range(N)]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                # 찾은 시작점에서 함수를 호출하고 break
                result = dfs(i, j)
                break

    print(f'#{tc} {result}')