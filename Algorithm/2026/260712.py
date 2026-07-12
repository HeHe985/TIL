'''
프로그래머스
코딩테스트 연습 월간 코드 챌린지 시즌2 괄호 회전하기
https://school.programmers.co.kr/learn/courses/30/lessons/76502
'''


def solution(s):
    answer = 0
    
    pair = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    
    n = len(s)
    
    for i in range(n):
        rotate = s[i:] + s[:i]
        stack = []
        
        for char in rotate:
            if char in "({[":
                stack.append(char)
            else:
                # 닫는 괄호인데 스택이 비었거나 or 괄호 짝 안맞으면 break
                if not stack or stack[-1] != pair[char]:
                    break
                # 닫는 짝 맞음
                stack.pop()
        else:
            if not stack:
                answer += 1
        
    return answer