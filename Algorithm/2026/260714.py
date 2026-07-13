'''
프로그래머스
코딩테스트 연습 2017 팁스타운 짝지어 제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/12973
'''

# 시간초과
def delete(s):
    len_s = len(s)
    for i in range(len_s - 1):
        if s[i] == s[i + 1]:
            return s[:i] + s[i + 2:]
    return s
        

def solution(s):
    answer = 0
    
    current_s = s
    while True:
        deleted_s = delete(current_s)
        
        if deleted_s == current_s:
            break
        elif len(deleted_s) == 0:
            answer = 1
            break
            
        current_s = deleted_s


    return answer


# stack으로 최적화
def solution(s):
    answer = 0
    
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if not stack:
        answer = 1

    return answer