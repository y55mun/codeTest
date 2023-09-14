""" 수 이어 쓰기 1
https://www.acmicpc.net/problem/1748
"""
n = int(input())
ans = str(1)
for i in range(2, n+1):
    ans += str(i)
print(len(ans))