""" 오큰수
https://www.acmicpc.net/problem/17298
"""
import sys
input = sys.stdin.readline

n = int(input())
ans = [-1] * n
a = list(map(int, input().split()))
stack = []

for i in range(n):
    while stack and a[stack[-1]] < a[i]:    # 스택이 비어있지 않고, 현재 수열이 스택 top 보다 클 경우
        ans[stack.pop()] = a[i]
    stack.append(i)

print(*ans)