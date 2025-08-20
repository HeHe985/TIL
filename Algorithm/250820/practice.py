# 원형 큐
class CircularQueue():
    # 생성자
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0

    # 큐가 비어있는지 확인
    def is_empty(self):
        return self.front == self.rear

    # 큐가 가득 찼는지 확인
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    # 삽입
    def enqueue(self, item):
        if self.is_full():
            raise IndexError('FULL')
        # rear +1
        self.rear = (self.rear + 1) % self.capacity
        # 큐 리스트의 새로운 rear에 저장
        self.items[self.rear] = item

    # 삭제
    def dequeue(self):
        if self.is_empty():
            raise IndexError('EMPTY')
        # front +1
        self.front = (self.front + 1) % self.capacity
        # 반환시 필요한 아이템 저장
        item = self.items[self.front]
        # 아이템 반환
        return item
    # 큐 요소 확인(삭제 X)
    def peek(self):
        if self.is_empty():
            raise IndexError('EMPTY')
        return self.items[(self.front + 1) % self.capacity]

    # 큐의 크기
    def get_size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

import sys
sys.stdin = open('5099.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    pizza_oven = CircularQueue(N)
    last_one = 0
    # 피자를 하나씩 집어 넣음
    for i in range(N):
        if pizza_oven.is_full() is False:
            pizza_oven.enqueue(C[i])
        else:
            for n in range(pizza_oven.get_size()):
                pizza_oven.items[n] //= 2
            if pizza_oven.get_size() > 1:
                for j in range(N):
                    if pizza_oven.items[j] == 0:
                        pizza_oven.items[j] = C[i]
                    else:
                        last_one = j


    result = last_one

    print(f'#{tc} {result}')