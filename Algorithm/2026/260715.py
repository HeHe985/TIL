'''
프로그래머스
코딩테스트 연습 탐욕법(Greedy) 구명보트
https://school.programmers.co.kr/learn/courses/30/lessons/42885
'''

# 시간초과
def solution(people, limit):
    answer = 0
    len_p = len(people)
    people = sorted(people, reverse=True)
    chk = [False] * len_p
    
    for i in range(len_p):
        if chk[i]:
            continue
        if people[i] >= limit:
            answer += 1
            chk[i] = True
            continue
            
        for j in range(i + 1, len_p):
            if chk[j]:
                continue
            if people[i] + people[j] <= limit:
                chk[i] = True
                chk[j] = True
                answer += 1
                break
        else:
            answer += 1
    
    return answer

# 성공
def solution(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1
    
    return answer