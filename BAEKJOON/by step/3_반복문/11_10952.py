""" A+B - 5_문자열
https://www.acmicpc.net/problem/10952
"""

while 1:
    a, b = map(int, input().split())

    if a==0 and b==0:
        break
    else:
        print(a+b)