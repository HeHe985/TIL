'''
프로그래머스
코딩테스트 연습 스택/큐 프로세스
https://school.programmers.co.kr/learn/courses/30/lessons/42587
'''

from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque([])
    
    for i in range(len(priorities)):
        q.append((priorities[i], i))

    while q:
        process, idx = q.popleft()
        
        if any(process < p for p, _ in q):
            q.append((process, idx))
        else:
            answer += 1
            if idx == location:
                return answer
            
    
    return answer