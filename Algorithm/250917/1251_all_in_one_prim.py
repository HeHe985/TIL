import sys
from heapq import heappush, heappop
sys.stdin = open('1251.txt')


def prim(start):
    visited = [0] * N
    pq = [(0, 0)]

    dists = [float('inf')] * N
    dists[0] = 0

    while pq:
        cost, node = heappop(pq)

        if visited[node]:
            continue




T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = int(input())



    # print(f'#{tc} {result}')