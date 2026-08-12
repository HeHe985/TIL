'''
정보올림피아드
연속된 최대값
https://jungol.co.kr/problem/1072
'''

n, m = map(int, input().split())

arr = list(map(int, input().split()))
answer = 0

for i in range(n - m + 1):
    answer = max(answer, sum(arr[i:i + m]))

print(answer)