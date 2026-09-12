'''
정보올림피아드
브라우저
https://jungol.co.kr/problem/1015
'''

forward_stack = []
backward_stack = []

url = "http://www.acm.org/"

while True:

    cmd = input()
    if cmd[0] == "B":
        if backward_stack:
            forward_stack.append(url)
            url = backward_stack.pop()
            print(url)
        else:
            print("Ignored")
    elif cmd[0] == "F":
        if forward_stack:
            backward_stack.append(url)
            url = forward_stack.pop()
            print(url)
        else:
            print("Ignored")
    elif cmd[0] == "V":
        backward_stack.append(url)
        _, url = cmd.split()
        print(url)
        forward_stack = []
    else:
        break
