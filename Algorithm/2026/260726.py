'''
프로그래머스
코딩테스트 연습 스택/큐 주식가격
https://school.programmers.co.kr/learn/courses/30/lessons/42584
'''

def solution(prices):
    
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
    
    while stack:
        idx = stack.pop()
        answer[idx] = n - 1 - idx
    
    return answer