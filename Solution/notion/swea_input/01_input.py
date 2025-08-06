import sys

sys.stdin = open('01_input.txt')

N, M = map(int, input().split)

# 일반 for문 방식
# 행의 개수만큼 반복해서 2차원 배열에 삽입
arr = []
for _ in range(N):
    # 행 생성
    # 예시: [1, 2, 3, 4]
    row = list(map(int, input().split()))
    arr.append(row)

# 리스트 컴프리헨션 방식

arr = [list(map(int, input().split) for _ in range(N))]