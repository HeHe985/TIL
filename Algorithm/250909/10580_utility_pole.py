import sys
sys.stdin = open('10580.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 첫번째 전봇대의 지점 기준으로 정렬
    arr.sort(key=lambda x: x[0])
    cnt = 0
    # 현재 지점부터 마지막 직전 지점까지 오른쪽 전봇대와 비교할 것임
    for i in range(N - 1):
        # 현재 지점의 오른쪽 부터 끝까지 자신보다 작다면 하나씩 세줌
        for j in range(i + 1, N):
            if arr[i][1] > arr[j][1]:
                cnt += 1

    print(f'#{tc} {cnt}')