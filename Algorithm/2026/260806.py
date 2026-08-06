'''
프로그래머스
코딩테스트 연습 동적계획법(Dynamic Programming) 정수 삼각형
https://school.programmers.co.kr/learn/courses/30/lessons/43105
'''

def solution(triangle):
    
    for row in range(len(triangle)):
        if row == 0:
            continue
        for col in range(len(triangle[row])):
            if col == 0:
                triangle[row][col] += triangle[row - 1][col]
            elif col == len(triangle[row]) - 1:
                triangle[row][col] += triangle[row - 1][col - 1]
            else:
                triangle[row][col] += max(triangle[row - 1][col - 1], triangle[row - 1][col])
    
    return max(triangle[-1])