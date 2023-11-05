""" 과제 안 내신 분..?
https://www.acmicpc.net/problem/5597
"""

students = list(range(1, 31))
submit = []

for i in range(1, 29):
    submit.append(int(input()))

ans = list(set(students) - set(submit))
ans.sort()
print(*ans, sep= '\n')