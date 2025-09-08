

#


'''
# Greedy2
people = [15, 30, 50, 10]
people.sort()

sum_waiting = 0

for i in range(len(people)):
    for j in range(i + 1, len(people)):
        sum_waiting += people[i]
print(sum_waiting)
'''

'''
# Greedy
coins = [500, 100, 50, 10]
target = 1730
cnt = 0

for coin in coins:
    coin_cnt = target // coin
    cnt += coin_cnt
    target -= coin * coin_cnt

print(cnt)
'''

'''
# 조힙
arr = ['A', 'B', 'C', 'D', 'E']
N = 3

path = []

def recur(cnt, start):
    if cnt == N:
        print(*path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(cnt + 1, i + 1)
        path.pop()
recur(0, 0)
'''

'''
# Binary Counting으로 부분집합 생성
arr = ['A', 'B', 'C']
n = len((arr))


def get_subset(target):
    for i in range(n):
        if target & 0x1:    # 가장 우측 비트를 체크, 왜 0x??: 비트연산임을 강조하는 암묵적인 룰
            print(arr[i], end=' ')
        target >>= 1


for tar in range(1 << n):
    get_subset(tar)
    print()
'''

# for i in range(1 << n):
#     for idx in range(n):
#         if i & (1 << idx):
#             print(arr[idx], end=' ')
#     print()
#

'''
# 완전탐색으로 부분집합 생성
name = ['MIN', 'CO', 'TIM']


def recur(cnt, subset):
    if cnt == 3:
        print(*subset)
        return

    # 부분집합에 포함 시키는 경우
    recur(cnt + 1, subset + [name[cnt]])
    # 포함 시키지 않는 경우
    recur(cnt + 1, subset)


recur(0, [])
'''