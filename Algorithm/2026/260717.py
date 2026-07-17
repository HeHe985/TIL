'''
프로그래머스
코딩테스트 연습 스택/큐 다리를 지나는 트럭
https://school.programmers.co.kr/learn/courses/30/lessons/42583
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    current_weight = 0
    time = 0
    
    while bridge:
        # 다리에서 하나씩 빠져 나감
        time += 1
        current_weight -= bridge.popleft()
        
        # 대기 트럭이 있을 경우
        if trucks:
            # 무게 조건이 맞을때 하나 추가
            if current_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                current_weight += truck
            # 아닐 경우에는 뒤에 0추가
            else:
                bridge.append(0)
        # 대기중 트럭 없고 현재 다리에 아무 트럭도 없으면 중지
        elif current_weight == 0:
            break
        else:
            bridge.append(0)

    return time