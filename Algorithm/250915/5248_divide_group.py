import sys
sys.stdin = open('5248.txt')
from collections import deque

# bfs
def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        current_node = q.popleft()
        for next_node in sorted(adj_list[current_node]):
            if visited[next_node]:
                continue
            visited[next_node] = True
            q.append(next_node)


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    adj_list = [[] for _ in range(N + 1)]
    cnt = 0
    visited = [False] * (N + 1)
    # 인접 리스트 생성
    for i in range(M):
        first = data[2 * i]
        second = data[2 * i + 1]

        adj_list[first].append(second)
        adj_list[second].append(first)

    # 1부터 N까지 방문하지 않았다면 cnt +1, bfs 실행
    for j in range(1, N + 1):
        if not visited[j]:
            cnt += 1
            bfs(j)

    print(f'#{tc} {cnt}')