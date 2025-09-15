import sys
sys.stdin = open('5248.txt')


# 대표자 찾기
def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


# 합집합
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # 같은 원소에 속해 있다면 리턴
    if root_x == root_y:
        return

    # 더 큰 랭크를 가진 집합의 루트에 연결
    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    elif rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    # 둘의 랭크가 같다면 한쪽에 추가하고 해당 랭크를 +1
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    parent = list(range(N + 1))
    rank = [0] * (N + 1)

    # 모든 쌍을 검사하여 합침
    for i in range(M):
        first, second = data[2 * i], data[2 * i + 1]
        union(first, second)

    # 루트 노드를 셋으로 선언
    root_nodes = set()
    # 1부터 N까지 순회하며 해당 노드의 루트노드를 set에 저장
    for i in range(1, N + 1):
        root_nodes.add(find_set(i))
    # 셋의 길이가 그룹의 수
    print(f'#{tc} {len(root_nodes)}')