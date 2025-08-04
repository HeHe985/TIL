import sys
sys.stdin = open('input_3.txt')

'''
리스트의 2번 부터 N-3까지의 건물 높이를 비교.
좌우로 2칸까지 비교하여 현재 기준의 건물 높이보다 높은 건물이 없을때 cnt +1
조망권이 확보된 세대 수는 현재 기준의 건물에서 좌/우의 건물 중 더 높은 건물의 높이를 뺀 값
'''

for tc in range(1, 11):
    # 조망권이 확보된 세대 수
    cnt = 0
    # 건물 개수
    N = int(input())
    # 건물 높이 리스트에 저장
    arr = list(map(int, input().split()))
    # 기준 건물 좌/우 중 가장 높은 건물의 높이
    # tallest = 0

    # 2부터 N-2 전까지 비교 필요
    for n in range(2, N-2):
        # 좌/우의 건물 높이 리스트
        height = [arr[n-2], arr[n-1], arr[n+1], arr[n+2]]
        # 리스트를 오름차순으로 버블정렬
        for i in range(3, 0, -1):
            for j in range(0, i):
                if height[j] > height[j+1]:
                    height[j], height[j+1] = height[j+1], height[j]
        # 좌/우로 두칸까지의 건물 높이중 최대 높이보다 현재 기준의 건물 높이가 더 높다면
        if height[3] < arr[n]:
            # 두 건물의 높이 차(조망권이 확보된 세대)만큼 cnt에 추가
            cnt += arr[n] - height[3]
    print(f'#{tc}', cnt)
