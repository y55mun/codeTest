""" 카드2
https://www.acmicpc.net/problem/2164
"""
from collections import deque

n = int(input())
queue = deque()

# 큐에 카드 저장
for i in range(1, n+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])