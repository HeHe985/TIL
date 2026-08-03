'''
프로그래머스
코딩테스트 연습 연습문제 점 찍기
https://school.programmers.co.kr/learn/courses/30/lessons/140107
'''

def solution(k, d):
    
    answer = 0
    
    for a in range(0, d + 1, k):
        max_b = int(((d - a) * (d + a)) ** 0.5)
        answer += max_b // k + 1
    
    return answer