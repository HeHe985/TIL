'''
프로그래머스
코딩테스트 연습 스택/큐 올바른 괄호
https://school.programmers.co.kr/learn/courses/30/lessons/12909
'''

def solution(s):
    answer = True
    
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        elif len(stack) != 0:
            prev = stack.pop()
        else:
            stack.append(i)
            break
            
    len_stack = len(stack)
    
    if len_stack != 0:
        answer = False
    
    return answer