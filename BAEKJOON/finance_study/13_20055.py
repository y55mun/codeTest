""" 컨베이어 벨트 위의 로봇
https://www.acmicpc.net/problem/20055


- 회전: deque 사용
- n개의 벨트만 로봇이 존재 => n 길이의 로봇 유무를 저장하는 배열 생성

1. 벨트 회전 => deque rotate
2. 로봇 이동
    - 가장 먼저 올라간 로봇부터 앞으로 이동
    - 다음 칸: 내구도 >= 1 and 로봇 X and 현재 로봇이 존재할때
3. 로봇 올리기: 올리는 위치에 내구도 != 0 and 로봇이 처음에 존재하지 X
4. 중지: count(내구도 == 0) >= k
"""

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
a = deque(map(int, input().split()))    # 내구도
robot = deque([0]*n)    # 벨트 위에 있는 로봇
result = 0

while a.count(0) < k:
    # if a.count(0) >= k:
    #     break

    a.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    for i in range(n-2, -1, -1):
        if a[i+1] >=1 and robot[i+1] == 0 and robot[i] == 1:
            robot[i+1] = 1
            robot[i] = 0
            a[i+1] -= 1
    robot[-1] = 0

    if a[0] !=0 and robot[0] != 1:
        robot[0] = 1
        a[0] -= 1
    result += 1


print(result)