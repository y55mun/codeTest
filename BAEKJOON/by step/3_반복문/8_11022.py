""" A+B - 8
https://www.acmicpc.net/problem/11022
"""

import sys
input = sys.stdin.readline

t = int(input())
# cases = [list(map(int, input().split())) for _ in range(t)]

for i in range(t):
    a,b = map(int, input().split())
    # print("Case #", i+1 ,": ", sum(cases[i]), sep='')
    # print("Case #", i+1 ,": ", cases[i][0], " + ", cases[i][1] , " = ",sum(cases[i]), sep='')
    print("Case #" + str(i+1)+":", a, "+", b, "=", a+b)

