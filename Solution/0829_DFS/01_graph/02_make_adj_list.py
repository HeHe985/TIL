import sys

sys.stdin = open('input.txt')


# --- 그래프 구성 (인접 리스트) ---
# 정점과 간선의 개수를 입력 받기
V, E = map(int, input().split())

# 간선 정보를 리스트 하나로 입력 받기
arr = list(map(int, input().split()))

# V+1개의 빈 리스트를 가지는 리스트를 생성
adj_list = [[] for _ in range(V + 1)]

# 간선의 개수만큼 반복하면서 2개씩 짝지어서 표기
for i in range(E):
    # 두 정점을 저장(n1과 n2는 서로 인접한 두 정점을 의미)
    n1, n2 = arr[2 * i], arr[2 * i + 1]

    # 정점 n1번 리스트에 n2 정점을 추가
    adj_list[n1].append(n2)
    # 무향 그래프이므로, 정점 n2번 리스트에도 n1 정점을 추가
    adj_list[n2].append(n1)

# --- 결과 확인 ---
for row in adj_list:
    print(row)