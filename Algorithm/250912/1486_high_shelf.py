import sys
sys.stdin = open('1486.txt')


# 높이가 B 이상이며, 높이가 가장 낮은 탑 찾기
def find_appropriate_top(height, n):
    global min_height
    # 높이가 B이상이 되면 최솟값 갱신
    if height >= B:
        min_height = min(min_height, height)
        return
    # 이미 최솟값을 넘어섰을 경우
    if height >= min_height:
        return
    # n명을 다 검사했을 경우 리턴
    if n == N:
        return
    # 요소에 포함
    find_appropriate_top(height + H[n], n + 1)
    # 미포함
    find_appropriate_top(height, n + 1)


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    min_height = 10000 * N
    find_appropriate_top(0, 0)

    print(f'#{tc} {min_height - B}')