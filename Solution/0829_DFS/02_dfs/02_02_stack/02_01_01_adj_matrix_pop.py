import sys

sys.stdin = open('input.txt')


def DFS_stack_pop_style(start):
    '''
    스택을 활용한 DFS (Pop 시점 방문 처리)
    '''
    visited = [False] * (V + 1)
    
    stack = [start]                 # 방문할 노드를 저장할 스택(시작 노드 삽입)
    result_path = []

    # 탐색 시작(스택이 빌 때까지)
    while stack:

        # 1. 스택에서 정점을 pop
        current_node = stack.pop()

        # 2. [핵심]: 스택에서 꺼낸 후, 방문했었는지 확인
        if not visited[current_node]:
            # 3. 방문 처리 및 경로 추가
            visited[current_node] = True
            result_path.append(current_node)

            # 4. 현재 정점과 인접한 정점들을 스택에 바로 삽입
            # V부터 1까지 역순으로 확인(작은 번호의 정점을 스택의 위쪽에 위치시키기 위함)
            # 만약 큰 번호의 정점을 우선적으로 방문하고 싶다면 정방향으로 스택에 push
            for next_node in range(V, 0, -1):
                if (
                    adj_matrix[current_node][next_node] == 1
                    and not visited[next_node]
                ):
                    # 5. 스택에 push
                    stack.append(next_node)

    return result_path


# --- 그래프 구성 ---
V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접행렬(Adjacency Matrix) 생성
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 간선 정보를 인접행렬에 기록 (양방향)
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

# --- DFS 실행 ---
result_path = DFS_stack_pop_style(1)
print(''.join(map(str, result_path)))
