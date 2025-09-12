import sys
sys.stdin = open('6190.txt')


# 단조증가인지 확인하는 함수
def is_monotone(num):
    # 자리수를 하나씩 추가할 예정
    num_list = []
    # 수가 0이 되면 탈출
    while num > 0:
        # 리스트에 10으로 나눈 나머지 추가하고 num을 몫으로 변경
        num_list.append(num % 10)
        num //= 10

    prev_num = 0
    # 리스트는 일의 자리부터 저장되기 때문에 거꾸로 순회
    for i in range(len(num_list) - 1, -1, -1):
        if prev_num > num_list[i]:
            return False
        prev_num = num_list[i]

    return True


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = -1

    for i in range(N):
        for j in range(i + 1, N):
            num = arr[i] * arr[j]
            if is_monotone(num):
                max_num = max(max_num, num)

    print(f'#{tc} {max_num}')
