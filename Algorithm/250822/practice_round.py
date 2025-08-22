import sys
sys.stdin = open('input.txt')


# 전위 순회 함수
def preorder(v):
    if v:
        print(v, end=' ')
        preorder(left_node[v])
        preorder(right_node[v])


# 중위 순회 함수
def inorder(v):
    if v:
        inorder(left_node[v])
        print(v, end=' ')
        inorder(right_node[v])


# 후위 순회 함수
def postorder(v):
    if v:
        postorder(left_node[v])
        postorder(right_node[v])
        print(v, end=' ')


V = int(input())
E = V - 1
edge = list(map(int, input().split()))

left_node = [0] * (V + 1)
right_node = [0] * (V + 1)

for e in range(E):
    # 부모/자식 노드 쌍
    parent, child = edge[2 * e], edge[2 * e + 1]
    # 왼쪽 자식 노드가 없다면 왼쪽에 저장
    if left_node[parent] == 0:
        left_node[parent] = child
    # 왼쪽 자식노드가 이미 있다면 오른쪽에 저장
    else:
        right_node[parent] = child

print('전위 순회')
preorder(1)
print('\n중위 순회')
inorder(1)
print('\n후위 순회')
postorder(1)

# print(left_node, right_node)