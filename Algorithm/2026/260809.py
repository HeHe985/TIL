'''
프로그래머스
코딩테스트 연습 그래프 순위
https://school.programmers.co.kr/learn/courses/30/lessons/49191
'''

from collections import deque


def bfs(win, lose, n, start):
    visited = [False] * (n + 1)
    visited[start] = True
    
    win_cnt, lose_cnt = 0, 0
    
    q = deque([])
    q.append(start)
    
    while q:
        winner = q.popleft()
        
        for next_node in win[winner]:
            if not visited[next_node]:
                visited[next_node] = True
                win_cnt += 1
                q.append(next_node)

                
    visited = [False] * (n + 1)
    visited[start] = True
    
    q = deque([])
    q.append(start)
    
    while q:
        loser = q.popleft()
        
        for next_node in lose[loser]:
            if not visited[next_node]:
                visited[next_node] = True
                lose_cnt += 1
                q.append(next_node)
    
    return win_cnt + lose_cnt


def solution(n, results):
    answer = 0
    
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]
    for result in results:
        n1, n2 = result[0], result[1]
        win[n1].append(n2)
        lose[n2].append(n1)
    
    for i in range(1, n + 1):
        if bfs(win, lose, n, i) == n - 1:
            answer += 1
    
    return answer