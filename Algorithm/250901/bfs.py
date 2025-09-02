import sys
from collections import deque
sys.stdin = open('bfs.txt')


def bfs(start):
    visited = [False] * (V + 1)
    path = []
    q = deque()

    # 시작 노드 방문처리, 큐에 삽입
    visited[start] = True
    q.append(start)

    # 큐가 빌 때까지
    while q:
        # 큐에서 첫 노드를 하나 꺼내 현재 노드에 저장
        current = q.popleft()
        # 경로에 추가
        path.append(current)

        # 현재 노드의 인접 노드 탐색
        for next_node in sorted(adj_list[current]):
            # 방문하지 않은 노드라면 방문처리, 큐에 추가
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)

    return path


V, E = map(int, input().split())
edges = list(map(int, input().split()))
adj_list = [[] for _ in range(V + 1)]

# 인접 노드 정보를 쌍으로 저장
for i in range(E):
    n1, n2 = edges[2 * i], edges[2 * i + 1]

    adj_list[n1].append(n2)
    adj_list[n2].append(n1)
# 시작 정점 부터
result = bfs(1)
print(''.join(map(str, result)))