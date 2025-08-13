import sys
sys.stdin = open('switch.txt')

# 스위치를 한번 눌렀을때 변화된 리스트를 반환하는 함수
def switch(li, n, index_n):
    # 1부터 1000까지 순회하며
    for i in range(1, 1001):
        # 갱신할 요소가 리스트의 범위 안일때만
        if index_n * i - 1 < n:
            # 현재 인덱스 값의 배수번쨰 인덱스의 값을 반전
            if li[index_n * i - 1] == 'Y':
                li[index_n * i - 1] = 'N'
            elif li[index_n * i - 1] == 'N':
                li[index_n * i - 1] = 'Y'
        else:
            break
    return li

T = 4

for tc in range(1, T + 1):
    list_input = list(input())
    N = len(list_input)
    cnt = 0
    num_N = list_input.count('N')

    for j in range(1, N + 1):
        # 꺼진 스위치 개수가 배열의 수와 같으면 break
        if num_N == N:
            result = cnt
            break
        else:
            # 스위치를 누를때 마다 리스트와 꺼진 스위치 개수, 스위치를 누른 횟수 변경
            list_input = switch(list_input, N, j)
            num_N = list_input.count('N')
            cnt += 1
    else:
        result = -1
    print(f'#{tc} {cnt}')