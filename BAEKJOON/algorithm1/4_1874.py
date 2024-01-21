""" 스택 수열
https://www.acmicpc.net/problem/1874
"""

n = int(input())
stack, ans, find = [], [], True

now = 1
for _ in  range(n):
    num = int(input())  # 현재 수열 값
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')

    else:
        find = False

if not find:
    print('NO')
else:
    for i in ans:
        print(i)