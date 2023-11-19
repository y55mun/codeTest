""" 색종이
https://www.acmicpc.net/problem/2563
"""

arr = [[0 for _ in range(101)] for _ in range(101)]
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

result = 0
for i in arr:
    result += i.count(1)

print(result)