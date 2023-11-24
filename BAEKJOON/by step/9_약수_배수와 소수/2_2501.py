""" 약수 구하기
https://www.acmicpc.net/problem/2501
"""

n, k = map(int, input().split())

tmp = []
for i in range(1, n+1):
    if n % i == 0:
        tmp.append(i)

if len(tmp) < k:
    print('0')
else:
    print(tmp[k-1])