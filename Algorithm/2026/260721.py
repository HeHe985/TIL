'''
프로그래머스
코딩테스트 연습 연습문제 최솟값 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12941
'''

# Greedy
def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]
            
    return answer

# 시간 초과
min_sum = 1000*1000*2


def dfs(visited_b, current_sum, idx_A, A, B):
    global min_sum
    if idx_A >= len(B):
        min_sum = min(current_sum, min_sum)
        return
    if current_sum >= min_sum:
        return
    for i in range(len(B)):
        if visited_b[i]:
            continue
        visited_b[i] = True
        dfs(visited_b, current_sum + A[idx_A] * B[i], idx_A + 1, A, B)
        visited_b[i] = False

def solution(A,B):
    
    visited_b = [False] * len(A)
    
    dfs(visited_b, 0, 0, A, B)
            
    return min_sum