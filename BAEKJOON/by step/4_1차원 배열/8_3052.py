""" 나머지
https://www.acmicpc.net/problem/3052
"""

nums = [int(input()) for _ in range(1,11)]
tmp = []

for i in nums:
    tmp.append(i % 42)

set(tmp)
print(len(set(tmp)))