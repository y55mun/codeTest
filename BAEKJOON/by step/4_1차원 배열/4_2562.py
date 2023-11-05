""" 최댓값
https://www.acmicpc.net/problem/2562
"""

cases = []

for i in range(9):
    cases.append(int(input()))

print(max(cases))
print(cases.index(max(cases)) + 1)