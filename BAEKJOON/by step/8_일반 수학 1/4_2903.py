""" 중앙 이동 알고리즘
https://www.acmicpc.net/problem/2903
"""

N = int(input())

ans = 2
for i in range(1, N+1):
    # ans = x + 2**(i-1)     # 거듭제곱 연산자를 몰랐다...
    ans += 2**(i-1)
print(ans**2)