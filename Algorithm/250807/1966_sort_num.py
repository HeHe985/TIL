import sys
sys.stdin = open('1966.txt')

T =  int(input())
'''
# 선택 정렬
def selection_sort(a, n):
    for i in range(0, n - 1):
        min_i = i
        for j in range(i + 1, n):
            if a[min_i] > a[j]:
                min_i = j
        a[min_i], a[i] = a[i], a[min_i]
    return a
'''

# 버블 정렬
def bubble_sort(a, n):
    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = " ".join(map(str, bubble_sort(arr, N)))
    print(f'#{tc} {result}')
