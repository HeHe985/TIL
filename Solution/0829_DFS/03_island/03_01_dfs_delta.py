import sys

sys.stdin = open("input.txt")


# 입력 처리
N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]

# 방문 여부
visited = [[False] * M for _ in range(N)]
print(visited)
# 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하(대각선 4방향)을 포함한 8방향 델타
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1,- 1, 1, -1, 1]

# DFS 함수 정의 (재귀 방식)
def dfs(r, c):
    # 현재 위치 방문 표시
    visited[r][c] = True
    # 현재 위치에서 8방향 이웃 확인
    for d in range(8):
        nr, nc = r + dr[d], c + dc[d]

        # 다음 이동 위치가 격자 범위 안에 있고,
        if 0 <= nr < N and 0 <= nc < M:
            # 그 곳이 땅(1)이면서, 내가 방문하지 않았다면,
            if grid[nr][nc] == 1 and not visited[nr][nc]:
                # 재귀적으로 탐색을 이어감
                dfs(nr, nc)


# --- 메인 로직 ---
island_count = 0

# 모든 칸을 하나씩 확인
for i in range(N):
    for j in range(M):
        # 현재 위치가 땅(1)이면서 아직 방문하지 않은 곳이라면
        if grid[i][j] == 1 and not visited[i][j]:

            # 새로운 섬을 발견한 것
            island_count += 1
            # 이섬과 연결된 모든 땅을 방문 처리하기 위해 DFS를 시작
            dfs(i, j)

# 최종 섬의 개수를 출력합니다.
print(island_count)
