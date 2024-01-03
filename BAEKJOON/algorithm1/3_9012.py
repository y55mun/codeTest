""" 괄호
https://www.acmicpc.net/problem/9012
"""

t = int(input())
stack = []

for _ in range(t):
    a = input().split()

    if a == '(':
        stack.append(a)
    elif a == ')':
        if stack:
            stack.pop()
        else:
            print("NO")
            break
