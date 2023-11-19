""" 행렬 덧셈
https://www.acmicpc.net/problem/2738
"""

n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(input().split())

for i in range(n):
    b.append(input().split())

c = []
for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end =' ')
    print()
