""" 분수찾기
https://www.acmicpc.net/problem/1193
"""

num = int(input())
line = 1

while num > line:
    num -= line     # 각 line 에서 n이 몇 번째에 위치하는지 알 수 있다.
    line += 1

# 짝수 일 때
if line % 2 == 0:
    a = num
    b = line - num + 1

# 홀수 일 때때
ele:
    a = line-num+1
    b = num

print(a,'/',b, sep='')