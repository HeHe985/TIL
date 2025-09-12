import sys
sys.stdin = open('9367.txt')

T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    # 직전 당근
    prev_carrot = 0
    cnt = 0
    max_cnt = 0
    # 당근 리스트를 돌며
    for carrot in carrots:
        # 이전 당근보다 지금이 더 크다면 +1
        if prev_carrot < carrot:
            cnt += 1
        # 작거나 같다면 cnt = 1로 초기화(자기자신 1)
        else:
            cnt = 1
        # 최댓값 갱신
        max_cnt = max(max_cnt, cnt)
        # 현재 당근을 이전 당근에 저장하고 넘어감
        prev_carrot = carrot

    print(f'#{tc} {max_cnt}')