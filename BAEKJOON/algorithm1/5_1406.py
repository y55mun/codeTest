"""에디터
https://www.acmicpc.net/problem/1406
"""

import sys

left = list(input())
right = []

for _ in range(int(input())):
    command = list(sys.stdin.readline().split())

    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

answer = left + right[::-1]
print(''.join(answer))