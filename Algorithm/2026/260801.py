'''
프로그래머스
코딩테스트 연습 깊이/너비 우선 탐색(DFS/BFS) 타겟 넘버
https://school.programmers.co.kr/learn/courses/30/lessons/43165
'''

answer = 0


def dfs(num, idx, numbers, target):
    global answer
    if idx == len(numbers):
        if num == target:
            answer += 1
        return
    
    dfs(num + numbers[idx], idx +1, numbers, target)
    dfs(num - numbers[idx], idx +1, numbers, target)
        

def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer