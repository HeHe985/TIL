'''
# 1. Merge Sort - 재귀


# 왼쪽, 오른쪽 배열을 정렬하며 병합하는 함수
def merge(left_arr, right_arr):
    merged_arr = []
    # 두 배열을 가리킬 포인터(인덱스) 초기화
    left_idx, right_idx = 0, 0

    # 두 배열 중 하나라도 원소가 남아있다면 반복(두 배열 중 하나라도 빌 때 까지)
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        # 왼쪽 배열의 값이 더 작거나 같으면, 결과에 추가하고 왼쪽 포인터 이동
        if left_arr[left_idx] <= right_arr[right_idx]:
            merged_arr.append(left_arr[left_idx])
            left_idx += 1
        # 오른쪽 배열의 값이 더 작으면, 결과에 추가하고 오른쪽 포인터 이동
        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1
    # 위의 while문이 끝나면 이미 한쪽 배열은 비어있으므로 남아있는 원소들을 결과 뒤에 붙여줌
    # 둘 중 하나만 실행됨
    merged_arr.extend(left_arr[left_idx:])
    merged_arr.extend(right_arr[right_idx:])

    return merged_arr


def merge_sort(arr):
    # 기저조건: 배열의 길이가 1이면 최소 단위로 나눈것. 이미 정렬된 상태
    if len(arr) <= 1:
        return arr

    # 1. 분할
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 2. 정복
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # 3. 통합
    return merge(left_sorted, right_sorted)


# --- 실행 코드 ---
data_array = [69, 10, 30, 2, 16, 8, 31, 22]
print(f'정렬 전: {data_array}')
sorted_array = merge_sort(data_array)
print(f'정렬 후 : {sorted_array}')
'''

'''
# 2. Merge Sort - 반복문(Bottom-Up 방식)


# arr[start, ..., mid]와 arr[mid + 1, ..., end]라는 두 정렬된 부분 배열을 하나로 정렬해 병합하는 함수
def merge_two_subarrays(arr, start, mid, end):
    merged = []
    left_idx = start
    right_idx = mid + 1

    while left_idx <= mid and right_idx <= end:
        if arr[left_idx] <= arr[right_idx]:
            merged.append(arr[left_idx])
            left_idx += 1
        else:
            merged.append(arr[right_idx])
            right_idx += 1

    # 남은 요소 붙이기
    while left_idx <= mid:
        merged.append(arr[left_idx])
        left_idx += 1

    while right_idx <= end:
        merged.append(arr[right_idx])
        right_idx += 1

    # 실제 arr에 병합 결과 반영                     # 같은 기능
    for i, val in enumerate(merged):             # for i in range(len(merged)):
        arr[start + i] = val                         # arr[start + i] = merged[i]


# 반복문으로 병합 정렬을 구현(Bottom-Up)
# 1. 길이 1씩 구간을 2개씩 합쳐 길이 2 정렬
# 2. 길이 2씩 구간을 2개씩 합쳐 길이 4 정렬
# 3. ...
def iterative_merge_sort(arr):
    n = len(arr)
    size = 1                    # 부분 배열의 크기: 1, 2, 4, 8, ...

    while size < n:
        # step 단위로 subarray를 병합
        for start in range(0, n, 2 * size):
            mid = start + size - 1
            end = min(start + 2 * size - 1, n - 1)

            # mid가 배열 범위 내라면 병합 수행행
            if mid < end < n:
                merge_two_subarrays(arr, start, mid, end)
        size *= 2


# --- 실행 코드 ---
data_array = [69, 10, 30, 2, 16, 8, 31, 22]
print(f'정렬 전: {data_array}')
iterative_merge_sort(data_array)
print(f'정렬 후 : {data_array}')
'''

'''
# 3. Quick sort - Lomuto Partition


# 분할
# 가장 오른쪽 원소를 피벗으로 설정
# 피벗이 있어야 할 올바른 위치의 인덱스 반환
def partition(arr, start, end):
    # 피벗을 가장 오른쪽 끝 요소로 설정
    pivot = arr[end]
    # 피벗보다 작은 원소들을 저장할 경계 인덱스 i
    i = start - 1

    # start 부터 end - 1까지 순회
    for j in range(start, end):
        # 현재 원소가 피벗 보다 작으면
        if arr[j] < pivot:
            # 작은 원소 그룹의 경계를 한 칸 오른쪽으로 이동
            i += 1
            # 경계(i)와 현재 원소(j)의 위치를 교환
            arr[i], arr[j] = arr[j], arr[i]
    # 모든 순회 를 마치면 i + 1 위치가 피벗이 들어갈 자리
    # 피벗과 경계 다음 위치의 값을 교환
    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    # 피벗의 최종 위치 인덱스를 반환
    return i + 1


# 퀵 정렬을 재귀적으로 구현
def quick_sort(arr, start, end):
    # 기저 조건: 원소가 1개 이하일 때는 중지
    if start < end:
        # 1. 분할: partition 함수 호출하여 피벗의 최종 위치 찾음
        pivot_idx = partition(arr, start, end)

        # 2-1. 정복: 피벗을 기준으로 나뉜 왼쪽 부분 정렬
        quick_sort(arr, start, pivot_idx - 1)
        # 2-2. 정복: 피벗을 기준으로 나뉜 오른쪽 부분 정렬
        quick_sort(arr, pivot_idx + 1, end)


# --- 실행 코드 ---
data_array = [3, 2, 4, 6, 9, 1, 8, 7, 5]
print(f'정렬 전: {data_array}')
quick_sort(data_array, 0, len(data_array) - 1)
print(f'정렬 후 : {data_array}')
'''


# 4. Quick Sort - Hoare Partition


# Hoare 파티션
# arr[start]를 피벗으로 사용
def partition_hoare(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end

    while True:
        # left 포인터 이동: 피벗보다 큰 값을 찾을 때까지
        while left <= end and arr[left] < pivot:
            left += 1
        # right 포인터 이동: 피벗보다 작은 값을 찾을 때까지
        while left <= right and arr[right] > pivot:
            right -= 1
        # 포인터가 교차했다면 반복 종료
        if left > right:
            break

        # 교차 전이면 두 값의 위치를 교환
        arr[left], arr[right] = arr[right], arr[left]

    # 마지막으로 피벗과 right 포인터가 가리키는 값을 교환
    # 이 코드로 인해 피벗은 항상 최종 위치를 반환함
    # 원래는 교환 안함
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort_hoare(arr, start, end):
    if start < end:
        pivot_idx = partition_hoare(arr, start, end)

        # 재귀 호출
        quick_sort_hoare(arr, start, pivot_idx - 1)
        quick_sort_hoare(arr, pivot_idx + 1, end)

# --- 실행 코드 ---
# data_array = [3, 2, 4, 6, 9, 1, 8, 7, 5]
data_array = [8, 3, 7, 6, 2, 5, 4]
print(f'정렬 전: {data_array}')
quick_sort_hoare(data_array, 0, len(data_array) - 1)
print(f'정렬 후 : {data_array}')