'''
프로그래머스
코딩테스트 연습 그래프 가장 먼 노드
https://school.programmers.co.kr/learn/courses/30/lessons/49189
'''

from collections import deque

def min_distance(start, n, adj_list):
    visited = [False] * (n + 1)
    visited[start] = True
    
    distance = [0] * (n + 1)
    
    q = deque([])
    q.append((start, 0))
    
    while q:
        node, dist = q.popleft()

        for next_node in adj_list[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, dist + 1))
                distance[next_node] = dist + 1
            
    return distance
                

def solution(n, edge):
    
    adj_list = [[] for _ in range(n + 1)]
    
    for e in edge:
        n1, n2 = e[0], e[1]
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)
    
    answer = min_distance(1, n, adj_list)
    
    return answer.count(max(answer))