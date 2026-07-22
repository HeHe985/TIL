'''
프로그래머스
코딩테스트 연습 연습문제 미로 탈출
https://school.programmers.co.kr/learn/courses/30/lessons/159993
'''

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(start, end, row, col, maps):
    
    visited = [[False] * col for _ in range(row)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, sec = queue.popleft()
        
        if end == (x, y):
            return sec
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < row and 0 <= ny < col:
                if maps[nx][ny] != "X" and not visited[nx][ny]:
                    queue.append((nx, ny, sec + 1))
                    visited[nx][ny] = True
        
    return -1


def solution(maps):
    row, col = len(maps), len(maps[0])
    
    for r in range(row):
        for c in range(col):
            if maps[r][c] == "S":
                start = (r, c)
            elif maps[r][c] == "L":
                lever = (r, c)
            elif maps[r][c] == "E":
                end = (r, c)
                
    # 1. 레버 찾기
    round1 = bfs(start, lever, row, col, maps)
    if round1 == -1 :
        return -1
    # 2. 출구 찾기
    round2 = bfs(lever, end, row, col, maps)
    if round2 == -1:
        return -1
    return round1 + round2

'''
프로그래머스
코딩테스트 연습 2019 KAKAO BLIND RECRUITMENT 오픈채팅방
https://school.programmers.co.kr/learn/courses/30/lessons/42888
'''

def solution(record):
    answer = []
    dic = {}
    for step in record:
        data = step.split()
        
        action = data[0]
        uid = data[1]
        
        if action == "Leave":
            continue
        
        else:
            dic[uid] = data[2]
            
    for step in record:
        data = step.split()
        if data[0] == "Change":
            continue
        elif data[0] == "Enter":
            answer.append(f'{dic[data[1]]}님이 들어왔습니다.')
        elif data[0] == "Leave":
            answer.append(f'{dic[data[1]]}님이 나갔습니다.')
    
    return answer