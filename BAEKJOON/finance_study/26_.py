""" [PCCP 모의고사 #2] 1번 - 실습용 로봇
https://school.programmers.co.kr/learn/courses/15009/lessons/121687
"""

def solution(command):
    dxy = [[0,1], [1,0], [0,-1], [-1, 0]]   # 12시, 3시, 6시, 9시 방향으로 회전
    x = 0   # x좌표
    y = 0   # y좌표
    dir = 0 # 방향 (dxy 배열의 dir 번째 배열을 선택해 좌표 이동)

    for c in command:
        if c == 'R':    # 오른쪽으로 회전
            dir = (dir+1)%4
        elif c == 'L':
            dir = (dir-1)%4
        elif c == 'G':
            x += dxy[dir][0]
            y += dxy[dir][1]
        else:
            x -= dxy[dir][0]
            y -= dxy[dir][1]
    return [x,y]