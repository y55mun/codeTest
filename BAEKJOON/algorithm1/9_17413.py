""" 단어 뒤집기 2
https://www.acmicpc.net/problem/17413
"""

stack = []
result = ''
check = False  # 괄호가 있는지 체크

data = input()

for i in data:

    if i == '<':
        check = True
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(i)

    if i == '>':
        check = False
        for _ in range(len(stack)):
            result += stack.pop(0)

    if i == ' ' and check == False:
        # stack.pop()
        for k in range(len(stack)):
            if k == 0:
                stack.pop()
                continue
            result += stack.pop()
        result += ' '

if stack:
    for _ in range(len(stack)):
        result += stack.pop()

print(result)