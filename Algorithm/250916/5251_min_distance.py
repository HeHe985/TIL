import sys
sys.stdin = open('5251.txt')
from heapq import heappush, heappop

def dijkstra(start):
    # 노드가 0 ~ N번 까지
    distance = [float('inf')] * (N + 1)
    pq = []

    distance[start] = 0
    heappush(pq, (0, start))

    while pq:
        # pq가 빌 때까지 하나씩 꺼내서 검사
        current_dist, current_node = heappop(pq)
        # 이미 더 적은 거리로 온적이 있다면 패스
        if current_dist > distance[current_node]:
            continue
        # 그래프의 인접 노드를 순회하며
        for next_dist, next_node in graph[current_node]:
            # 새 거리를 계산하고
            new_dist = current_dist + next_dist
            # 새로 계산한 거리가 이미 저장된 값보다 크거나 같으면 패쓰
            if new_dist >= distance[next_node]:
                continue
            # 아니면 갱신하고 힙에 추가
            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return distance

T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        start, end, distance = map(int, input().split())
        graph[start].append((distance, end))

    result_arr = dijkstra(0)

    print(f'#{tc} {result_arr[N]}')