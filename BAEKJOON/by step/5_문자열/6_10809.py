""" 알파벳 찾기
https://www.acmicpc.net/problem/10809
"""

voca = list(input())
c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in voca:
        print(voca.index(i), end = ' ')
    else:
        print(-1, end=' ')