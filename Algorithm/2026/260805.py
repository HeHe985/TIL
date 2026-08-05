'''
프로그래머스
코딩테스트 연습 동적계획법(Dynamic Programming) N으로 표현
https://school.programmers.co.kr/learn/courses/30/lessons/42895
'''

def solution(N, number):
    
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                
                    if y != 0:
                        dp[i].add(x // y)
        if number in dp[i]:
            return i

    return -1