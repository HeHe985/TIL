'''
프로그래머스
코딩테스트 연습 연습문제 숫자 변환하기
https://school.programmers.co.kr/learn/courses/30/lessons/154538
'''

from collections import deque


def bfs(start, end, n):
    visited = set()
    visited.add(start)
    queue = deque([])
    queue.append((start, 0))
    
    while queue:
        x, cnt  = queue.popleft()
        if x == end:
            return cnt
        for num in [x + n, x * 2, x * 3]:
            if not num in visited and num <= end:
                queue.append((num, cnt + 1))
                visited.add(num)
        
    return -1
    

def solution(x, y, n):
    answer = bfs(x, y, n)
    return answer