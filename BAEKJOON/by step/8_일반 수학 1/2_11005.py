""" 진법 변환 2
https://www.acmicpc.net/problem/11005

10진수 N -> B진법로 바꿔 출력
"""

N, B = map(int, input().split())
system = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = ''
while N:
    ans += str(system[N%B])
    N //= B

print(ans[::-1])
