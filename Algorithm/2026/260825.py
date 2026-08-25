'''
프로그래머스
코딩테스트 연습 Summer/Winter Coding(~2018) 배달
https://school.programmers.co.kr/learn/courses/30/lessons/12978
'''

import heapq
def dij(start, N, adj_list, K):
    hq = []
    distance = [float('inf')] * (N + 1)
    
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]:
            continue
            
        if dist > K:
            break
            
        for adj_node, weight in adj_list[node]:
            new_dist = dist + weight
            if new_dist < distance[adj_node]:
                distance[adj_node] = new_dist
                heapq.heappush(hq, (new_dist, adj_node))
    return distance
    
    
def solution(N, road, K):
    answer = 0
    
    adj_list = [[] for _ in range(N + 1)]
    
    for r in road:
        adj_list[r[0]].append((r[1], r[2]))
        adj_list[r[1]].append((r[0], r[2]))
        
    dist = dij(1, N, adj_list, K)
    
    for i in range(1, N + 1):
        if dist[i] <= K:
            answer += 1
    
    return answer