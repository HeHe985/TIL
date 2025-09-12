import sys
sys.stdin = open('5207.txt')


def binary_search(arr, target, left, right, status):
    # 타깃을 찾지 못할 경우
    if left > right:
        return False

    mid = (left + right) // 2
    # 찾을 경우
    if arr[mid] == target:
        return True
    # 타깃이 mid 값보다 작을 경우
    elif arr[mid] > target:
        # 현재 상태가 left면 False
        if status == 'left':
            return False
        # 아닐 경우 재귀 호출
        return binary_search(arr, target, left, mid - 1, 'left')
    # 타깃이 mid 값보다 클경우
    else:
        # 현재 상태가 right면 False
        if status == 'right':
            return False
        # 아닐 경우 재귀호출
        return binary_search(arr, target, mid + 1, right, 'right')


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    result = 0
    # B의 요소를 하나씩 검사하며
    for i in B:
        # 재귀 호출의 반환값이 참인 경우 세어줌
        if binary_search(A, i, 0, N - 1, 'none'):
            result += 1

    print(f'#{tc} {result}')