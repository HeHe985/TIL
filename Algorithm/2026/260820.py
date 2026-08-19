'''
프로그래머스
코딩테스트 연습 힙(Heap) 이중우선순위큐
https://school.programmers.co.kr/learn/courses/30/lessons/42628
'''

import heapq


def solution(operations):

    heap = []
    
    for operation in operations:
        if operation.startswith("I"):
            heapq.heappush(heap, int(operation[2:]))
        elif heap:
            if operation.startswith("D -1"):
                heapq.heappop(heap)
            else:
                heap = [-x for x in heap]
                heapq.heapify(heap)
                heapq.heappop(heap)
                heap = [-x for x in heap]
                heapq.heapify(heap)
    
    if heap:
        return [max(heap), min(heap)]
    else:
        return [0, 0]