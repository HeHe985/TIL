'''
프로그래머스
코딩테스트 연습 Summer/Winter Coding(~2018) 방문 길이
https://school.programmers.co.kr/learn/courses/30/lessons/49994?language=python3
'''

directions = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0)
}

def solution(dirs):
    x, y = 0, 0
    
    visited = set()
    answer = 0
    
    for d in dirs:
        nx, ny = x + directions[d][0], y + directions[d][1]
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue
            
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            answer += 1
        x, y = nx, ny
            
    return answer