'''
프로그래머스
코딩테스트 연습 탐욕법(Greedy) 큰 수 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/42883
'''

def solution(number, k):
    answer = ''
    
    stack = []
    for char in number:
        while stack and k > 0 and stack[ -1] < char:
            stack.pop()
            k -= 1
        stack.append(char)
    if k > 0:
        stack = stack[:-k]
    answer = ''.join(stack)
    
    return answer