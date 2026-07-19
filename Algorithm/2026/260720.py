'''
프로그래머스
코딩테스트 연습 깊이/너비 우선 탐색(DFS/BFS) 게임 맵 최단거리
https://school.programmers.co.kr/learn/courses/30/lessons/1844
'''

# BFS
from collections import deque

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(start_x, start_y, visited, N, M, maps):
    queue = deque([(start_x, start_y, 1)])
    visited[start_x][start_y] = True
    
    while queue:
        x, y, distance = queue.popleft()
        
        if x == N - 1 and y == M - 1:
            return distance
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            
            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, distance + 1))
    return -1

def solution(maps):
    
    N, M = len(maps), len(maps[0])
    
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    
    answer = bfs(0, 0, visited, N, M, maps)
    
    return answer


# DFS는 시간초과
# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

min_distance = 10000

def dfs(x, y, distance, N, M, visited, maps):
    global min_distance
    
    if x == N - 1 and y == M - 1:
        min_distance = min(min_distance, distance)
        return
    
    if distance >= min_distance:
        return
    
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, distance + 1, N, M, visited, maps)
            visited[nx][ny] = False
    


def solution(maps):
    answer = 0
    
    N, M = len(maps), len(maps[0])
    
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    
    dfs(0, 0, 1, N, M, visited, maps)
    
    if min_distance != 10000:
        answer = min_distance
    else:
        answer = -1
    
    return answer