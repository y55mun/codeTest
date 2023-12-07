""" 좋은 단어
https://www.acmicpc.net/problem/3986
"""

n = int(input())
ans = 0

for _ in range(n):
    s = input()
    stack = []

    for i in range(len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])

    if not stack:
        ans += 1

print(ans)
