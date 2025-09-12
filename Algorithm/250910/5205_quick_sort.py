import sys
sys.stdin = open('5205.txt')


# quick sort Lomuto
def quick_sort(start, end, arr):
    if start < end:
        # 피벗의 위치 찾기
        pivot_idx = partition(start, end, arr)
        # 찾은 위치를 기준으로 좌/우로 쪼개서 다시 검사
        quick_sort(start, pivot_idx - 1, arr)
        quick_sort(pivot_idx + 1, end, arr)


def partition(start, end, arr):
    # 맨 오른쪽 요소를 피벗으로 설정
    pivot = arr[end]
    # 경계(포인터)를 처음 -1로 지정
    i = start - 1

    # 맨처음 부터 피벗 전(end - 1)까지 검사
    for j in range(start, end):
        # 피벗보다 작은 값을 찾으면
        if arr[j] < pivot:
            # 포인터를 우측르로 한칸 옮기고 , 해당 값 교환
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # 반복 종료 후, 피벗 위치 고정
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    # 피벗 인덱스 반환
    return i + 1


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    quick_sort(0, N - 1, data)
    print(f'#{tc} {data[N // 2]}')