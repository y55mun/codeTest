""" 코딩은 체육과목 입니다
https://www.acmicpc.net/problem/25314
"""

n = int(input())
m = 0
ans = "long int"

if n == 4:
    print(ans)
else:
    m = (n // 4) - 1
    print( m *("long ")+ans)
