from collections import deque
import sys
sys.stdin = open('5097.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 입력값 deque로 저장
    list_q = deque(map(int, input().split()))
    # M번 왼쪽으로 로테이션
    list_q.rotate(-M)
    # 맨 앞의 숫자
    result = list_q.popleft()

    print(f'#{tc} {result}')