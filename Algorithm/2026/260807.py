'''
프로그래머스
코딩테스트 연습 동적계획법(Dynamic Programming) 등굣길
https://school.programmers.co.kr/learn/courses/30/lessons/42898
'''

def solution(m, n, puddles):

    arr = [[0] * (m + 1) for _ in range(n + 1)]
    arr[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            elif [j, i] in puddles:
                arr[i][j] = 0
            elif i == 1:
                arr[i][j] = arr[i][j - 1]
            elif j == 1:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = arr[i][j - 1] + arr[i - 1][j]
    
    return arr[-1][-1] % 1000000007