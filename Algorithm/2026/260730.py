'''
프로그래머스
코딩테스트 연습 완전탐색 최소직사각형
https://school.programmers.co.kr/learn/courses/30/lessons/86491
'''

def solution(sizes):
    w, h = 0, 0
    for s in sizes:
        if s[0] < s[1]:
            w, h = max(w, s[1]), max(h, s[0])
        else:
            w, h = max(w, s[0]), max(h, s[1])
    
    return w * h