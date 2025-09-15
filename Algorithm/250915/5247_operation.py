import sys
sys.stdin = open('5247.txt')
from collections import deque

def bfs(start):
    q = deque()
    q.append([start, 0])
    visited = {start}

    while q:
        current_num, cnt = q.popleft()
        # M과 같아지면 cnt 반환
        if current_num == M:
            return cnt
        next_cnt = cnt + 1

        # +1 연산
        next_num = current_num + 1
        # 범위 안의 값이고 아직 방문하지 않았다면
        if 0 < next_num <= 1000000 and next_num not in visited:
            # 방문처리, 큐에 추가
            visited.add(next_num)
            q.append((next_num, next_cnt))

        # -1 연산
        next_num = current_num - 1
        if 0 < next_num <= 1000000 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, next_cnt))

        # *2 연산
        next_num = current_num * 2
        if 0 < next_num <= 1000000 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, next_cnt))

        # -10 연산
        next_num = current_num - 10
        if 0 < next_num <= 1000000 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, next_cnt))


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    result = bfs(N)

    print(f'#{tc} {result}')