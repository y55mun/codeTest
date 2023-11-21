""" 벌집
https://www.acmicpc.net/problem/2292
"""

N = int(input())
nums = 1

for i in range(N):
    nums += i*6

    if N<nums:
        print(i+1)
        break