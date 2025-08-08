'''

'''

import sys
sys.stdin = open('1221.txt')

T = int(input())

order_li = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T + 1):
    n_tc, len_tc = input().split()
    arr = list(input().split())
    n_arr = [''] * int(len_tc)
    result = [''] * int(len_tc)

    for i in range(int(len_tc)):
        for j in range(10):
            if arr[i] == order_li[j]:
                n_arr[i] = j
    n_arr.sort()
    for k in range(int(len_tc)):
        for l in range(10):
            if n_arr[k] == l:
                result[k] = order_li[l]
    print(n_tc)
    print(*result)




