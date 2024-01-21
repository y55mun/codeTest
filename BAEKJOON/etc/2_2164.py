"""카드2
풀이 날짜: 24-01-21
https://www.acmicpc.net/problem/2164
"""

from collections import deque
n = int(input())
dq = deque()

for i in range(1, n+1):
    dq.append(i)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])
