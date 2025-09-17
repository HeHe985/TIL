import sys
from heapq import heappush, heappop
sys.stdin = open('mst_input.txt')


def prim(start=1):
    visited = [False] * (V + 1)
    pq = []

    mst_cost = 0
    edges_cnt = 0

    # 1. 시작 정점과 연결된 모든 간선을 우선순위 큐에 넣음
    for cost, next_node in adj_list[start]:
        heappush(pq, (cost, start, next_node))
    visited[start] = True

    # 2. 큐가 비거나 MST가 완성될 때까지 반복
    while pq and edges_cnt < V - 1:
        # 3. 현재 MST 집합과 연결된 간선 중 , 가장 가중치가 낮은 간선을 꺼냄
        cost, _, end = heappop(pq)

        # 4. 도착 정점이 이미 MST에 포함된 경우, 이 간선은 사이클을 유발하므로 무시
        if visited[end]:
            continue

        # 5. 새로운 정점을 MST에 포함
        visited[end] = True
        mst_cost += cost
        edges_cnt += 1

        # 6. 새로 추가된 정점과 연결된, 아직 방문 안 한 정점으로 가는 간선들을 큐에 추가
        for next_cost, next_node in adj_list[end]:
            if not visited[next_node]:
                heappush(pq, (next_cost, end, next_node))

    return mst_cost


V, E = map(int, input().split())

adj_list = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, cost = map(int, input().split())
    adj_list[s].append((cost, e))
    adj_list[e].append((cost, s))

result_cost = prim(start=1)
print(result_cost)

'''
import sys
sys.stdin = open('mst_input.txt')
from heapq import heappush, heappop

# 특정 정점 기준 시작
# 갈 수 있는 노드들 중 가장 작은 노드부터 간다
# 작은 노드를 먼저 꺼내기위해 우선순위 큐(heapq)를 활용
def prim(start_node):
    # (가중치, 노드) 형태: 가중치가 앞인 이유는 정렬 등 기준이 앞 요소이기 때문
    pq = [(0, start_node)]
    # visited와 종일한 역할
    MST = [0] * V
    # 최소 비용
    min_weight = 0

    while pq:
        # 가장 작은 가중치 꺼내짐
        weight, node = heappop(pq)
        # 이미 방문한 노드라면 continue
        if MST[node]:
            continue
        # 노드로 가는 최소비용이 선택됨
        MST[node] = 1
        # 가중치 누적 합
        min_weight += weight
        for next_node in range(V):
            if graph[node][next_node] == 0:
                continue
            # 이미 방문 했으면 지나감
            if MST[next_node]:
                continue
            # 원래 BFS에서는 여기서 방문 처리함
            # BUT, MST에서 여기서 하면 최소비용 안됨
            heappush(pq, (graph[node][next_node], next_node))

    return min_weight


V, E = map(int, input().split())
# 1. 인접 행렬
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    # 무향 그래프
    graph[start][end] = weight
    graph[end][start] = weight
# 출발 정점을 바꾸어도 최소비용은 같음
# 단, 그래프는 다를 수 있음
result = prim(0)
print(result)
'''