'''
def KFC(x):
    if x == 4:
        return
    print(x)
    KFC(x + 1)
    print(x)


KFC(0)
print('끝')
'''

'''
def run(x):
    if x == N:
        return
    result.append(x)
    run(x + 1)
    result.append(x)

N = 6
result = []
run(0)
print(result)
'''

'''
중복 순열
[0, 1, 2] 3개의 카드 중 2개 뽑기

path = []
N = 3
# 기저조건: 2개의 카드를 모두 뽑았다면 종료
# 시작점: 0개의 카드를 고른 상태
# 다음 재귀호출 구조: 카드 중 하나를 고른다
def recur(cnt):
    if cnt == 2:
        print(path)
        return

    # 카드 중 하나를 선택
    for i in range(N):
        path.append(i)
        recur(cnt + 1)
        path.pop()

recur(0)
'''

'''
path = []
N = 3
used = [False] * (N+1)
# 기저조건: 2개의 카드를 모두 뽑았다면 종료
# 시작점: 0개의 카드를 고른 상태
# 다음 재귀호출 구조: 카드 중 하나를 고른다
def recur(cnt):
    if cnt == 2:
        print(path)
        return

    # 카드 중 하나를 선택
    for i in range(1, N + 1):
        if i in path:
            continue
        path.append(i)
        recur(cnt + 1)
        path.pop()

recur(0)
'''

'''
# 누적합을 활용
def recur(cnt, total):
    global result
    if total > 10:
        return
    if cnt == 3:
        # if total <= 10:           없어도 되지만 있어도 괜찮음
        #   result += 1
        result += 1
        return

    # 카드 중 하나를 선택
    for i in range(1, N + 1):
        recur(cnt + 1, total + i)



result = 0

path = []
N = 6
recur(0, 0)
print(result)
'''

# 트럼프: 카드 다섯장 뽑았을 때 같은 종류의 카드가 3장 연속으로 나오는 경우의 수

cards = ["A", "J", "Q", "K"]
path = []
result = 0


# 연속된 3개의 같은 카드가 나오면 리턴 True 아니면 False
def is_three():
    return


def recur(cnt):
    global result

    if cnt == 5:
        # Todo: 연속된 3개가 나오면 카운팅
        if is_three():
            result += 1
            print(*path)
        return
    # 4개릐 카드 중 하나를 선택
    # 범용적으로 쓰기위해
    for idx in range(len(cards)):
        path.append(cards[idx])
        recur(cnt + 1)
        path.pop()


recur(0)

