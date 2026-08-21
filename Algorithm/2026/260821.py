'''
프로그래머스
코딩테스트 연습 Summer/Winter Coding(~2018) 점프와 순간 이동
https://school.programmers.co.kr/learn/courses/30/lessons/12980
'''

def solution(n):
    ans = 0
    while n != 0:
        if n % 2 == 0:
            n /= 2
        else:
            ans += 1
            n -= 1

    return ans