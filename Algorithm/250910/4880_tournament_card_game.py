import sys
sys.stdin = open('4880.txt')


def tournament(start, end):
    # 요소가 1개가 되면 종료
    if start == end:
        return start

    mid = (start + end) // 2
    # 왼쪽 반, 오른쪽 반 다시 나눠 검사
    left_winner = tournament(start, mid)
    right_winner = tournament(mid + 1, end)

    # 왼쪽과 오른쪽의 승자를 반환
    return find_winner(left_winner, right_winner)


# 가위바위보 승자의 인덱스 반환함수
def find_winner(left, right):
    if data[left] == data[right]:
        return min(left, right)
    elif (data[left] == 1 and data[right] == 3) or (data[left] == 2 and data[right] == 1) or (data[left] == 3 and data[right] == 2):
        return left
    else:
        return right


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    result = tournament(0, N - 1)

    print(f'#{tc} {result + 1}')