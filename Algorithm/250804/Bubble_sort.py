# Bubble 정렬

'''
bublle_sort(arr, N):    # 정렬할 배열 arr, arr의 크기 N
    for i : N-1 -> 1   # (배열의 크기 - 1) 만큼 반복
        for j : 0 -> i-1    # 비교할 두개의 요소중 왼쪽 요소의 인덱스
            if arr[j] > arr[j+1]:   # 두 요소 중 오른쪽 요소가 더 크면
                arr[j], arr[j+1] = arr[j+1], arr[j] # 두 요소 교환
'''
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):  # 정렬할 마지막 요소 인덱스
        for j in range(0, i):   # 값을 비교할 두 요소중 왼쪽 인덱스
            if arr[j] > arr[j+1]:   # 값 비교 후 왼쪽 요소가 더 큰 경우 값 교환
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)