'''
프로그래머스
코딩테스트 연습 깊이/너비 우선 탐색(DFS/BFS) 단어 변환
https://school.programmers.co.kr/learn/courses/30/lessons/43163
'''

from collections import deque


def bfs(begin, target, words):
    visited = set()
    q = deque([(begin, 0)])
    visited.add(begin)
    
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for w in words:
            n = 0
            for i in range(len(word)):
                if word[i] == w[i]:
                    n += 1
            if n == len(word) - 1 and not w in visited:
                q.append((w, cnt + 1))
                visited.add(w)
    return 0
        

def solution(begin, target, words):
    
    return bfs(begin, target, words)