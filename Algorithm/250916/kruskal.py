import sys
sys.stdin = open('mst_input.txt')


def find_set(parent, x):
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    root_x = find_set(parent, x)
    root_y = find_set(parent, y)

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


def kruskal_mst(num_vertives, edges):
    # 1. 간선들을 가중치(cost) 기준으로 오름차순 정렬
    edges.sort()

    # 2. Union-Find를 위한 parent 리스트 초기화(각자 자신이 대표)
    parent = [i for i in range(num_vertives + 1)]

    # MST의 총 가중치
    mst_cost = 0
    # MST에 포함된 간선의 수
    edges_cnt = 0

    # 3. 가장 가중치가 낮은 간선부터 순회
    for cost, s, e in edges:
        # 4. 두 정점의 대표가 다른지 확인(사이클 생성 여부 체크)
        if find_set(parent, s) == find_set(parent, e):
            continue
        # 5. 사이클이 생기지 않으면, 간선을 MST에 포함시키고 두 정점을 같은 집합으로 합침(union)
        union(parent, s, e)
        mst_cost += cost
        edges_cnt += 1

        # MST는 V - 1개의 간선으로 이루어지므로, 다 찾았으면 종료
        if edges_cnt == num_vertives - 1:
            break

    return mst_cost


V, E = map(int, input().split())
edges_info = []
for _ in range(E):
    # (가중치, 시작, 끝) 형태로 저장
    s, e, cost = map(int, input().split())
    edges_info.append((cost, s, e))
    print(edges_info)

result_cost = kruskal_mst(V, edges_info)
print(result_cost)

'''
import sys
sys.stdin = open('mst_input.txt')


def find_set(x):
    if x == parents[x]:
        return x
    # 기본 코드
    #return find_set(parents[x])
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    # 사이클 발생
    if rx == ry:
        return

    # 일정한 규칙, 작은 수로
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

V, E = map(int, input().split())

# 1. 간선들을 가중치 기준으로 정렬
edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    # 간선들의 정보 저장
    edges.append((start, end, weight))

# 가중치 기준 오름차순 정렬
edges.sort(key=lambda x: x[2])

# 2. 가중치가 작은 간선부터 순서대로 선택
# 사이클이 발생하면 고르지 않음
# MST가 완성될 때까지: V - 1개를 선택할 때까지

# 현재까지 선택한 간선의 수
cnt = 0
# 가중치의 합
result = 0


# make_set
parents = [i for i in range(V)]



for u, v, w in edges:
    # 사이클이 아니라면 연결(같은 집합으로 만든다)
    # 연결하면서 cnt + 1, cnt가 V - 1이면 종료
    if find_set(u) != find_set(v):
        union(u, v)
        cnt += 1
        result += w

        if cnt == V - 1:
            break
print(result)
'''