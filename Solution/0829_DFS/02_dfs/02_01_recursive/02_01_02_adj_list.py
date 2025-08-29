import sys

sys.stdin = open('input.txt')


def dfs_recursive_list(current_node, adj_list, visited, path):
    """
    인접 리스트와 재귀를 이용한 DFS
    """
    # 1. 현재 정점을 방문처리 & 경로 추가
    visited[current_node] = True
    path.append(current_node)

    # 2. 현재 정점에 인접한 정점들을 직접 순회
    # 인접 행렬처럼 모든 정점를 확인할 필요없이, 인접한 정점을 바로 탐색 가능
    for next_node in adj_list[current_node]:
        # 인접 정점이 아직 방문하지 않았다면 재귀 호출 진행
        if not visited[next_node]:
            dfs_recursive_list(next_node, adj_list, visited, path)


# --- 그래프 구성 ---
V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_list = [[] for _ in range(V + 1)]

for i in range(E):
    n1, n2 = arr[2 * i], arr[2 * i + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# --- DFS 실행 ---
visited = [False] * (V + 1)
result_path = []

# 1번 정점부터 탐색 시작
dfs_recursive_list(1, adj_list, visited, result_path)

print(result_path)