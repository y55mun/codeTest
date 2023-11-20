""" 세탁소 사장 동혁
https://www.acmicpc.net/problem/2720
"""

T = int(input())

for _ in range(T):
    C = int(input())
    for i in [25,10,5,1]:
        print(C//i, end = ' ')
        C %= i