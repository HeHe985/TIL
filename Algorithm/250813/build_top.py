import sys
sys.stdin = open('build_top.txt')

T = int(input())
for tc in range(1, T + 1):
    K, W1, W2 = map(int, input().split())
    tops = list(map(int, input().split()))
    # 가벼운 순으로 정렬
    tops.sort()
    # 최소 비용을 저장할 변수
    min_cost = 0
    # 화물 리스트를 순회하며
    for n in tops:
        # 더 높은 쪽으로 가벼운 순 화물을 배치했을때 비용을 min_cost에 더함
        if W1 >= W2:
            min_cost += n * W1
            W1 -= 1
        else:
            min_cost += n * W2
            W2 -= 1

    print(f'#{tc} {min_cost}')