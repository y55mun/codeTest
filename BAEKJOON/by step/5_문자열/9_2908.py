""" 상수
https://www.acmicpc.net/problem/2908
"""

a, b = map(str, input().split())
reverse_a = ''.join(list(a)[::-1])
reverse_b = ''.join(list(b)[::-1])

ans = 0
if reverse_a > reverse_b:
    ans = int(reverse_a)
else:
    ans = int(reverse_b)

print(ans)



# tmp = [int(i) for i in str(input())[::-1]]




