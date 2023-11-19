""" 최댓값
https://www.acmicpc.net/problem/2566
"""

a = [list(map(int, input().split())) for _ in range(9)]

max_value = max(map(max, a))
print(max_value)

for i in range(9):
    for j in range(9):
        if a[i][j] == max_value:
            print(i+1, j+1)