

# find: x의 최종 대표(루트)를 찾을 때까지 부모를 계속 따라 올라감
def find_set(parent, x):
    # 만약 x의 부모가 자기 자신이 아니라면,
    if parent[x] != x:
        # 재귀적으로 루트를 찾고, 그 루트를 나의 부모로 직접 설정
        parent[x] = find_set(parent, parent[x])
    return parent[x]


# union: 두 원소 x, y의 대표를 찾아, y의 대표를 x의 대표 밑으로 연결
def union(parent, rank, x, y):
    # 각 원소의 대표(루트)를 찾음
    root_x = find_set(parent, x)
    root_y = find_set(parent, y)
    # 두 원소가 이미 같은 집합에 속해 있다면 합칠 필요 없음
    if root_x == root_y:
        return
    # 랭크(트리 높이)가 더 낮은 쪽을 더 높은 쪽 밑에 붙임
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        # 랭크가 같다면, 한쪽을 다른 쪽에 붙이고 랭크를 1 증가시킴
        parent[root_y] = root_x
        rank[root_x] += 1


# --- 실행 예시 ---
V = 5 # 1부터 5까지의 원소
parent = [i for i in range(V + 1)] # 각자 자기 자신을 부모로 초기화
rank = [0] * (V + 1)               # 모든 원소의 랭크를 0으로 초기화

# {1}, {2}, {3}, {4}, {5}
union(parent, rank, 1, 3) # {1,3}, {2}, {4}, {5}
union(parent, rank, 2, 4) # {1,3}, {2,4}, {5}
union(parent, rank, 3, 4) # {1,2,3,4}, {5}

# 1과 4가 같은 그룹에 속해 있는지 확인
print(f"find_set(1) => {find_set(parent, 1)}")
print(f"find_set(4) => {find_set(parent, 4)}")
print(f"1과 4는 같은 그룹인가? {find_set(parent, 1) == find_set(parent, 4)}")

# 1과 5가 같은 그룹에 속해 있는지 확인
print(f"1과 5는 같은 그룹인가? {find_set(parent, 1) == find_set(parent, 5)}")