import sys
sys.stdin = open('5174.txt')


# 전위 순회로 호출 횟수를 계산하는 함수
def cnt_preorder(r):
    # 함수가 호출될 때마다 전역 변수 cnt +1
    global cnt
    if r:
        cnt += 1
        cnt_preorder(left[r])
        cnt_preorder(right[r])


T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))

    V = E + 1

    left = [0] * (V + 1)
    right = [0] * (V + 1)
    # 함수 호출 횟수를 세줄 변수
    cnt = 0
    # 왼/오른쪽 자식 노드 정보 각각 저장
    for e in range(E):
        parent, child = edge[2 * e], edge[2 * e + 1]

        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child
    # print(left, right)
    cnt_preorder(N)

    print(f'#{tc} {cnt}')