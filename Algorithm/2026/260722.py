'''
프로그래머스
코딩테스트 연습 연습문제 JadenCase 문자열 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12951
'''

def solution(s):
    answer = ''
    
    for i, char in enumerate(s):
        if i == 0 or s[i - 1] == " ":
            answer += char.upper()
        else:
            answer += char.lower()
    
    return answer