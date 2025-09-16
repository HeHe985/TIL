import sys
sys.stdin = open('dijkstra_input.txt')
from heapq import heappop, heappush


def dijkstra(start_node):
    # (누적거리, 노드 번호)
    pq = [(0, start_node)]
    # 각 정점까지의 최단거리를 저장할 리스트
    dists = [INF] * V
    # 시작노드 최단거리는 0
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)

        # 이미 더 작은 값으로 온 적이 있으면 버린다
        # (3, c), (4, c) 예시
        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            # 다음 노드로 가기 위한 누적 거리 계산
            # 누적 거리 = 현재까지의 거리 + 다음 거리
            new_dist = dist + next_dist

            # 이미 작거나 같은 가중치로 온 적이 있다면 넘어감
            if dists[next_node] <= next_dist:
                continue

            # 누적 거리와, 새로운 노드를 pq에 저장, dists에 갱신
            dists[next_node] = next_dist
            heappush(pq, (next_dist, next_node))

    return dists


INF = int(21e8)

V, E = map(int, input().split())
# 시작점 노드
start_node = 0
# 인접 리스트로 구현
graph = [[] for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    # 주의! 단방향
    graph[start].append((weight, end))

# 출발지로부터 모든 최단 거리
result = dijkstra(0)
print(result)