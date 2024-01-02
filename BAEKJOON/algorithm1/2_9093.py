""" 단어 뒤집기
https://www.acmicpc.net/problem/9093
"""

t = int(input())

for _ in range(t):
    str = input().split()

    for i in str:
        print(i[::-1], end=' ')
