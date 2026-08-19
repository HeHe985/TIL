'''
프로그래머스
코딩테스트 연습 힙(Heap) 디스크 컨트롤러
https://school.programmers.co.kr/learn/courses/30/lessons/42627
'''

import heapq

def solution(jobs):
    
    # 반환시간 누적
    answer = 0
    
    jobs.sort()
    
    # 다음 작업의 index
    job = 0
    
    # 대기큐: 소요시간, 요청시각
    heap = []
    
    # 현재 시간
    t = 0
    
    # 마지막 작업까지 or 힙이 비어있지 않다면(대기큐에 해야 할 작업이 남아있다면) 반복
    while job < len(jobs) or heap:
        
        # 현재 시간까지 요청된 모든 작업을 대기 큐에 추가
        while job < len(jobs) and jobs[job][0] <= t:
            request, duration = jobs[job]
            heapq.heappush(heap, (duration, request))
            job += 1
        
        # 대기큐에 작업이 없다면
        if not heap:
            
            # 시간을 다음 작업의 요청시간으로 바로 이동
            t = jobs[job][0]
            continue
            
        # 대기큐에서 우선순위가 가장 높은 작업 하나 꺼냄
        duration, request = heapq.heappop(heap)
        
        # 작업을 수행(소요시간 누적)
        t += duration
        
        # 반환시간 = 작업종료 시각 - 작업 요청 시각
        answer += t - request
        
    
    return answer // len(jobs)