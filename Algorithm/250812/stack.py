
# 1번 방법
'''
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

stack.pop()
stack.pop()
stack.pop()
'''

stack = [0] * 10
top = -1
# push
def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow')
        return 0
    else:
        stack[top] = item
# pop
def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top + 1]

push(1, 10)
push(2, 10)
push(3, 10)

print(stack)

print(pop())
print(pop())
print(pop())