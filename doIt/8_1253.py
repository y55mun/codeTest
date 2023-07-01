""" 좋은 수 구하기
https://www.acmicpc.net/problem/1253

투포인터
"""
import sys
input = sys.stdin.readline

n = int(input())
res = 0
a = list(map(int, input().split()))

a.sort()

for i in range(n):
    s = 0
    e = n-1

    find = a[i]
    while s < e:
        if a[s] + a[e] == find:
            if s != i and e != i:
                res += 1
                break
            elif s == i:
                s += 1
            elif e == i:
                e -= 1
        elif a[s] + a[e] < find:
            s += 1
        else:
            e -= 1
print(res)



