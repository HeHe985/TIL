import sys
sys.stdin = open('practice_quick.txt')


# 퀵 정렬 - 로무토
def quick_sort(start, end, arr):
    # 기저 조건: 원소가 1개 이하일때
    if start < end:

        pivot_idx = partition(start, end, arr)

        # 피벗 왼쪽
        quick_sort(start, pivot_idx - 1, arr)
        # 피벗 오른쪽
        quick_sort(pivot_idx + 1, end, arr)


# 피벗을 설정하고 피벗 위치 확정
def partition(start, end, arr):
    # 피벗을 오른쪽 끝 값으로
    pivot = arr[end]
    # 포인터(경계)
    i = start - 1

    for j in range(start, end):
        # 피벗보다 작은값 찾으면 i +1, 값 교환
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # 모든 순회 마치고 경계의 다음과 끝 값(피벗) 교환
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    # 피벗 위치 반환
    return i + 1


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    quick_sort(0, len(data) - 1, data)
    print(f'#{tc} {data}')