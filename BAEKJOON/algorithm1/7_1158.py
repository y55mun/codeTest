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
        dq.append(dq.popleft()) # dq의 왼쪽 값을 빼서 다시 append 함으로써 제거해야 할 k번째 수를 제일 왼쪽에 배치
    ans.append(dq.popleft())    # k번째 수를 제거해서 정답 배열에 추가

print(str(ans).replace('[', '<').replace(']','>'))
