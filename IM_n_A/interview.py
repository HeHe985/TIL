import sys
sys.stdin = open('interview.txt')

def fac(num):
    fac_result = 1
    for n in range(1, num + 1):
        fac_result *= n
    return fac_result


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    bit_part = []
    for i in range(N):
        bit_part.append(bin(i))

    print(bit_part)
answer = []
score = [0] * N
cnt = 0
total_score = 0
if answer[i] == 0:
    cnt = 0
    score[i] = 0
elif cnt == K:
    score[i] = 1
    cnt = 0
    total_score *= 2
else:
    cnt += 1
    score[i] = 1




if (N / 2) // 2 <= M:
    pass
else:
    pass






    # size_part = fac(N)/(fac(N - M) * fac(M))
    #
    # for i in range(size_part):
    #     pass





    # print(f'${tc} {result}')