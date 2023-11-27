""" 소수
https://www.acmicpc.net/problem/2581
"""

m = int(input())
n = int(input())
ans = []

for i in range(m, n+1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count += 1
                break
        if count == 0:
            ans.append(i)


if len(ans) > 0:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)