import sys
sys.stdin = open('5201.txt')

'''
N: 컨테이너 수
M: 트럭 수
weight: i번 컨테이너 화물의 무게
capacity: j번 트럭의 적재 용량
'''

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    capacity = list(map(int, input().split()))

    # 화물무게는 내림차순, 트럭의 적재용량은 오름차순 정렬
    weight.sort(reverse=True)
    capacity.sort()
    # 결과를 저장할 무게 합 변수
    sum_weight = 0
    # 트럭의 적재용량이 적은 것부터
    for truck in capacity:
        # 무게가 무거운 화물 부터 차례로 들어가는지 검사 후
        for n in range(len(weight)):
            # 들어간다면, 결과에 무게를 더해주고 해당 화물을 리스트에서 제거한 후 반복문 빠져나감
            if truck >= weight[n]:
                sum_weight += weight[n]
                weight.pop(n)
                break

    print(f'#{tc} {sum_weight}')