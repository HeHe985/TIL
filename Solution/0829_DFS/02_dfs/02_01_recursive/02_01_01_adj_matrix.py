import sys

sys.stdin = open('input.txt')


def dfs_recursive_matrix(current_node, adj_matrix, visited, path):
    """
    특정 노드를 시작으로 연결된 모든 노드를 재귀적으로 탐색하고,
    탐색 경로를 path 리스트에 추가합니다.

    Args:
        current_node (int): 현재 방문(탐색)하고 있는 노드
        adj_matrix (list): 그래프의 인접 행렬
        visited (list): 노드 방문 여부를 기록하는 리스트
        path (list): 탐색한 노드 순서를 기록할 리스트
    """
    # 1. 현재 노드 방문처리 / 경로에 추가
    visited[current_node] = True
    path.append(current_node)
    # 2. 현재 노드와 인접한 다른 노드들을 순회
    # V는 adj_matrix의 크기(len)로 알 수 있으므로, 전역변수 V에 의존하지 않음
    for next_node in range(1, len(adj_matrix)):
        # 현재 노드와 인접해 있고(1), 아직 방문하지 않았는지(2)
        # 1번과 2번 조선을 만족하면 탐색 가능(재귀 호출 가능)
        if adj_matrix[current_node][next_node] == 1 and not visited[next_node]:
            dfs_recursive_matrix(next_node, adj_matrix, visited, path)
"""
입력을 받아 그래프(인접 행렬)를 생성하고,
DFS를 수행하여 최종 탐색 경로를 반환하는 메인 로직
"""


# --- 그래프 구성 ---
# 정점과 간선의 개수를 입력 받기
V, E = map(int, input().split())

# 간선 정보를 리스트 하나로 입력 받기
arr = list(map(int, input().split()))

# V+1 * V+1 크기의 2차원 리스트를 0으로 초기화
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 양방향 간선 기록
for i in range(E):
    n1, n2 = arr[2 * i], arr[2 * i + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

# --- DFS 실행 ---
visited = [False] * (V + 1)         # 방문 여부 기록 리스트
result_path = []                    # 전체 탐색 경로를 저장할 리스트

# 1번 노드부터 시작
dfs_recursive_matrix(1, adj_matrix, visited, result_path)

# 전체 탐색 경로 출력
print(result_path)
# --- 모든 노드를 시작점으로 시도하는 경우 (그래프가 비연결일 경우를 대비) ---
# 그래프가 {1-2}, {3-4} 처럼 나뉘어 있다면 3, 4번 노드는 절대 방문하지 못함
# for i in range(1, V + 1):
#     if not visited[i]:
#         # i번 노드를 시작으로 하는 DFS 수행
#         dfs_recursive_matrix(i, adj_matrix, visited, traversal_path)
# print(''.join(map(str, traversal_path)))
