'''
프로그래머스
코딩테스트 연습 완전탐색 피로도
https://school.programmers.co.kr/learn/courses/30/lessons/87946
'''

answer = 0
def dfs(dungeons, cnt, visited, remain):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if not visited[i]:
            if remain >= dungeons[i][0]:
                visited[i] = True
                dfs(dungeons, cnt + 1, visited, remain - dungeons[i][1])
                visited[i] = False

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    
    dfs(dungeons, 0, visited, k)
    return answer