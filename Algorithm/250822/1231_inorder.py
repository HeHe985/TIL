import sys
sys.stdin = open('1231.txt')


# 중위 순회 함수
def inorder(r):
    if r:
        inorder(left[r])
        # 인덱스 -> 문자값 변환하여 결과값에 추가
        result.append(values[r])
        inorder(right[r])


T = 10

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    E = N - 1
    node_info = [input().split() for _ in range(N)]
    lst_inorder = []
    result = []
    # print(node_info)

    # <노드: 인덱스, 해당 노드의 문자: 값> 리스트
    values = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    # 정점 정보 한 세트씩 확인
    for i in node_info:
        values[int(i[0])] = i[1]
        # 리스트 크기가 2 초과이면 왼쪽 자식을 가짐
        if len(i) > 2:
            left[int(i[0])] = int(i[2])
        # 리스트 크기가 3 초과이면 오른쪽 자식을 가짐
        if len(i) > 3:
            right[int(i[0])] = int(i[3])
    inorder(1)
    print(f'#{tc}', ''.join(result))