""" 오큰수
푼 날짜: 24-01-21
https://www.acmicpc.net/problem/17298
"""

n = int(input())
ans = [-1] * n
a = list(map(int, input().split()))
stack = []

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        ans[stack.pop()] = a[i]
    stack.append(i)


print(*ans)