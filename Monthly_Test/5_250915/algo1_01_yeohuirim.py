# import sys
# sys.stdin = open('algo1_sample_in.txt')

# 단순 증가 패턴인지 확인해서 T/F로 반환하는 함수
def is_increasing(arr):
    # 이전 숫자를 저장할 prev
    prev = 0
    # 인자로 받은 배열의 요소를 하나씩 순회하며
    for i in arr:
        # 이전 요소보다 크다면 prev에 현재 요소를 저장
        if prev < i:
            prev = i
        # 이전 요소보다 작거나 같다면 바로 False를 반환
        else:
            return False
    # False가 반환되지 않고 순회를 마쳤다면 True 반환
    return True


T = int(input())
# 테스트케이스 반복문
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 단순 증가 패턴을 보이는 윈도우의 수를 저장할 cnt
    cnt = 0

    # 0부터 N까지 M스텝씩 순회하며
    for j in range(0, N, M):
        # 윈도우를 만들고
        part_list = A[j:j + M]
        # 해당 윈도우를 is_increasing() 함수로 단순증가 패턴을 보이는 지 검사
        if is_increasing(part_list):
            # 함수의 반환값이 True이면 cnt +1
            cnt += 1

    print(f'#{tc} {cnt}')
