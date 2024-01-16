"""요세푸스 문제
https://www.acmicpc.net/problem/1158

아이디어
k-1 개 빼고 다시 뒤에 붙이고, k번째를 pop
"""
from collections import deque

n, k = map(int,input().split())
dq = deque(range(1, n+1))

ans = []

while dq:
    for _ in range(k-1):
        dq.append(dq.popleft())
    ans.append(dq.popleft())

print(str(ans).replace('[', '<').replace(']','>'))
