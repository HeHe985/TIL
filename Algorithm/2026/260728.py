'''
프로그래머스
코딩테스트 연습 스택/큐 기능개발
https://school.programmers.co.kr/learn/courses/30/lessons/42586
'''

def solution(progresses, speeds):
    answer = []
    works = []
    for i in range(len(speeds)):
         works.append((100 - progresses[i] + speeds[i] - 1) // speeds[i])

    complete = works[0]
    cnt = 0
    
    for j in range(len(speeds)):
        if works[j] <= complete:
            cnt += 1
        else:
            answer.append(cnt)
            complete = works[j]
            cnt = 1
            
    answer.append(cnt)
    return answer
