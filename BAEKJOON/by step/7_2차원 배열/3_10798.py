""" 세로읽기
https://www.acmicpc.net/problem/10798
걸린시간: 44ms
"""

c = [[0]*15 for i in range(5)]

for i in range(5):
    d = list(input())
    for j in range(len(d)):
        c[i][j] = d[j]

for i in range(15):
    for j in range(5):
        if c[j][i] == 0:
            continue
        else:
            print(c[j][i], end='')




"""
방법 2
걸린시간: 44ms
"""

words = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')