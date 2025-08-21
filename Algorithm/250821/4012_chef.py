import itertools
import sys
sys.stdin = open('4012.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]







    print(f'#{tc} {min_sum}')







'''
    idx = [i for i in range(N)]
    p_idx = itertools.permutations(idx, N)
    min_sum = float('inf')
    for i in p_idx:
        data = []
        for j in i:
            data.append(arr[0][j])
            # print('D = ', data)
        food_a = data[:N // 2]
        food_b = data[N // 2:]
        # for j in range(int(N / 2)):
        #     food_a.append(arr[j])
        #     food_b.append(arr[j + int(N / 2)])

        # print(food_a)
        sum_a = sum(food_a)
        sum_b = sum(food_b)

        diff = abs(sum_a - sum_b)
        if min_sum > diff:
            min_sum = diff

'''
