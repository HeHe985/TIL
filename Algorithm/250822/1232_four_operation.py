import sys
sys.stdin = open('1232.txt')

# # 후위 순회 함수
# def inorder(v):
#     if v:
#         inorder(left[v])
#         lst_result.append(values[v])
#         inorder(right[v])

def calculate(node):
    if len(node_info[node]) == 2:
        return int(node_info[node][1])

    if node_info[node][1] == '+':
        return calculate(int(node_info[node][2])) + int(node_info[node][3])
    elif node_info[node][1] == '-':
        return int(node_info[node][2]) - int(node_info[node][3])
    elif node_info[node][1] == '*':
        return int(node_info[node][2]) * int(node_info[node][3])
    elif node_info[node][1] == '/':
        return int(node_info[node][2]) // int(node_info[node][3])

T = 10

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    E = N - 1

    node_info = [[0]]
    for _ in range(N):
        node_info.append(list(input().split()))

    print(calculate(1))


    # # 숫자인 값 int로 변환
    # for i in node_info:
    #     i[0] = int(i[0])
    #     if len(i) == 2:
    #         i[1] = int(i[1])
    #     else:
    #         i[2], i[3] = int(i[2]), int(i[3])
    # lst_result = [] * (N + 1)
    # # print(node_info)
    # values = [''] * (N + 1)
    # left = [0] * (N + 1)
    # right = [0] * (N + 1)
    #
    # for n in node_info:
    #     values[n[0]] = n[1]
    #     if len(n) == 4:
    #         left[n[0]] = n[2]
    #         right[n[0]] = n[3]
    #
    # inorder(1)
    # print(lst_result)




    # print(f'#{tc} {result}')