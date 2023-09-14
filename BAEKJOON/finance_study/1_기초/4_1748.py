""" 수 이어 쓰기 1
https://www.acmicpc.net/problem/1748
"""
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
ans = 0
for i in range(len(str(n))-1):
    ans += 9*(10**i) * (i+1)
ans += (int(n) - 10**(len(str(n))-1) + 1) * len(str(n))
print(ans)