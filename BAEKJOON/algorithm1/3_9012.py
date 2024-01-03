""" 괄호
https://www.acmicpc.net/problem/9012
"""

t = int(input())


for _ in range(t):
    stack = []
    a = input()

    for j in a:
        if j == '(':
            stack.append(a)
        elif j == ')':
            if stack:
                stack.pop()
            else:   # 스택에 괄호가 없을 경우
                print("NO")
                break
    else:   # break 문으로 끊기지 않고 수행됐을 경우 수행
        if not stack:   # 스택이 비어 있으면 괄호가 다 맞음
            print("YES")
        else:   # break 안걸었어도 스택에 괄호가 들어가 있다면 NO
            print("NO")
