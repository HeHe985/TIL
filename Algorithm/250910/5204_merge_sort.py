import sys
sys.stdin = open('5204.txt')

# 병합 & 정렬
def merge(left, right):
    global result
    left_idx, right_idx = 0, 0
    sorted_arr = []

    # 두 배열의 마지막 원소 비교
    if left[-1] > right[-1]:
        result += 1

    # 둘 중 한쪽이라도 빌때까지 계속
    while left_idx < len(left) and right_idx < len(right):
        # 왼쪽이 더 작다면 왼쪽 추가
        if left[left_idx] <= right[right_idx]:
            sorted_arr.append(left[left_idx])
            left_idx += 1
        # 오른쪽이 더 작으면 오른쪽 추가
        else:
            sorted_arr.append(right[right_idx])
            right_idx += 1

    # 반복문 종료후 남은 요소 전부 추가
    sorted_arr.extend(left[left_idx:])
    sorted_arr.extend(right[right_idx:])

    return sorted_arr


# 분할해서 병합 정렬
def merge_sort(arr):
    # 크기 1이면 재귀 종료
    if len(arr) <= 1:
        return arr

    # 둘로 분할
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 계속 쪼개기
    left_arr = merge_sort(left)
    right_arr = merge_sort(right)

    # 정렬해서 병합
    return merge(left_arr, right_arr)

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    sorted_arr = merge_sort(arr)

    half = sorted_arr[N // 2]

    print(f'#{tc} {half} {result}')