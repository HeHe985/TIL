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


# 2. 인접 리스트