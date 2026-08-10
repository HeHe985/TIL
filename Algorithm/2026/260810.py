'''
프로그래머스
코딩테스트 연습 깊이/너비 우선 탐색(DFS/BFS) 여행경로
https://school.programmers.co.kr/learn/courses/30/lessons/43164
'''

def dfs(departure, path, tickets, visited):
    # 모든 티켓 사용, 탈출
    if len(path) == len(tickets) + 1:
        return True
    
    # 사용할 수 있는 티켓 순회하며 사용 & 경로에 추가
    for i in range(len(tickets)):
        # 이미 사용한 티켓 or 출발지가 현재 공항이 아니면 건너뜀
        if visited[i] or tickets[i][0] != departure:
            continue
        
        # 사용처리 & 도착지를 경로에 추가
        visited[i] = True
        path.append(tickets[i][1])
        
        if dfs(tickets[i][1], path, tickets, visited):
            return True
        
        path.pop()
        visited[i] = False
    
    return False
    

def solution(tickets):
    tickets.sort()
    visited = [False] * len(tickets)
    
    answer = ["ICN"]
    dfs("ICN", answer, tickets, visited)
    return answer