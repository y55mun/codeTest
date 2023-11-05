""" 문자열
https://www.acmicpc.net/problem/9086
"""

T = int(input())

for i in range(T):
    voca = input()
    print(voca[0],voca[-1], sep='')