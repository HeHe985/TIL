import sys
sys.stdin = open('16811.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    carrots = sorted(list(map(int, input().split())))

    min_diff = 1000

    # 1. 빈 상자가 있어서는 안됨
    for i in range(N - 2):
        for j in range(i + 1, N - 1):

            # 2. 같은 크기의 당근은 같은 상자에 담아야 함
            if carrots[i] == carrots[i + 1] or carrots[j] == carrots[j + 1]:
                continue

            small = i + 1
            medium = j - i
            large = N - (j + 1)

            # 3. 한 상자에 N//2개를 초과하면 안됨
            if small > N // 2 or medium > N // 2 or large > N // 2:
                continue

            # 4. 개수 차이를 최소로 만들고 이때의 개수 차이를 출력
            diff = max(small, medium, large) - min(small, medium, large)
            min_diff = min(min_diff, diff)

    # 5. 포장할 수 없다면 -1 출력
    if min_diff == 1000:
        min_diff = -1

    print(f'#{tc} {min_diff}')