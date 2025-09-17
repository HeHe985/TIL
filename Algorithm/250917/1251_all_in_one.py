import sys
sys.stdin = open('1251.txt')


def calculate_square_length(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


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


def mst_kruskal(v, edges):
    # 간선 정렬
    edges.sort()

    # parent 초기화
    parent = [i for i in range(v)]

    total_cost = 0
    edges_cnt = 0

    for cost, start, end in edges:
        if find_set(parent, start) == find_set(parent, end):
            continue
        union(parent, start, end)
        total_cost += cost
        edges_cnt += 1

        if edges_cnt == v - 1:
            break

    return total_cost

T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    # 간선 정보 리스트 생성
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            edges.append((calculate_square_length(X[i], Y[i], X[j], Y[j]), i, j))

    result = (mst_kruskal(N, edges)) * E

    print(f'#{tc} {result: .0f}')