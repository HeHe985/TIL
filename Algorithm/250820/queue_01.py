# 리스트
'''
# 비어있는 큐
my_queue = []

# 삽입
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)

# 삭제
print(my_queue.pop(0))
print(my_queue.pop(0))
print(my_queue.pop(0))
'''
# deque
'''
from collections import deque

# 비어있는 큐
dq = deque([])

# 삽입
dq.append(1)
dq.append(2)
dq.append(3)

# 삭제
print(dq.popleft())
print(dq.popleft())
print(dq.popleft())
'''
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

my_queue = CircularQueue(5)
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())

