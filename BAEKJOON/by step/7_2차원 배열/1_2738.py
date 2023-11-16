""" 행렬 덧셈
https://www.acmicpc.net/problem/2738
"""

n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    # a.append(input().split())
    a.append(list(map(int, input().split())))

for i in range(n):
    # b.append(input().split())
    b.append(list(map(int, input().split())))


c = []
for i in range(n):
    for j in range(m):
        # c.append(int(a[i][j]) + int(b[i][j]))
        c.append(int(a[i][j]) + int(b[i][j]))
        # c[i][j] = int(a[i][j]) + int(b[i][j])
        # print(int(a[i][j]) + int(b[i][j]))
        print(a[i][j] + b[i][j], end =' ')
    print()
