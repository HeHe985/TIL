import sys
sys.stdin = open('5249.txt')


def find_set(parent, x):
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    root_x, root_y = find_set(parent, x), find_set(parent, y)

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


def kruskal(v, edges):
    # 가중치 기준 오름차순 정렬
    edges.sort()
    # 자기자신을 대표자로 지정
    parent = [i for i in range(v + 1)]

    total_cost = 0
    edges_cnt = 0

    # 넘겨받은 간선 정보를 순회
    for cost, n1, n2 in edges:
        # n1과 n2의 대표가 같다면 = 하나의 집합이라면 = 사이클을 형성한다면 넘어감
        if find_set(parent, n1) == find_set(parent, n2):
            continue
        # 아니라면 두 집합을 합치고 비용을 더함, 간선 개수 +1
        union(parent, n1, n2)
        total_cost += cost
        edges_cnt += 1

        # 노드 번호가 0 ~ V번 까지이므로 간선 개수는 V게 여야함
        if edges_cnt == v:
            break

    return total_cost


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))

    result = kruskal(V, edges)

    print(f'#{tc} {result}')