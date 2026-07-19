'''
프로그래머스
코딩테스트 연습 완전탐색 카펫
https://school.programmers.co.kr/learn/courses/30/lessons/42842
'''

def solution(brown, yellow):
    '''
    w * h = brown + yellow
    (w - 2) * (h - 2) = yellow
    '''
    total = brown + yellow
    for h in range(3, int(total ** 0.5) + 1):
        if total % h != 0:
            continue
        w = total // h
        
        if (w - 2) * (h - 2) == yellow:
            return [w, h]
