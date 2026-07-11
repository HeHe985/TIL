'''
프로그래머스
코딩테스트 연습 연습문제 다음 큰 숫자
https://school.programmers.co.kr/learn/courses/30/lessons/12911
'''

def solution(n):
    answer = n
    cnt_one = bin(n).count("1")
    while True:
        answer += 1
        if cnt_one == bin(answer).count("1"):
            break
    
    
    return answer