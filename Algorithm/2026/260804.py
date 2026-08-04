'''
프로그래머스
코딩테스트 연습 정렬 H-Index
https://school.programmers.co.kr/learn/courses/30/lessons/42747
'''

def solution(citations):
    citations.sort()
    n = len(citations)
    
    for i, citation in enumerate(citations):
        h = n - i
        if citation >= h:
            return h

    return 0