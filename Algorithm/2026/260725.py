'''
프로그래머스
코딩테스트 연습 연습문제 N-Queen
https://school.programmers.co.kr/learn/courses/30/lessons/12952
'''

def dfs(x, visited, n, diag1, diag2):
    if x >= n:
        return 1
    
    answer = 0
    
    for y in range(n):
        if not visited[y] and not diag1[x - y] and not diag2[x + y]:
            visited[y] = True
            diag1[x - y] = True
            diag2[x + y] = True

            answer += dfs(x + 1, visited, n, diag1, diag2)

            visited[y] = False
            diag1[x - y] = False
            diag2[x + y] = False
            
    return answer


def solution(n):
    visited = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    answer = dfs(0, visited, n, diag1, diag2)
    
    return answer