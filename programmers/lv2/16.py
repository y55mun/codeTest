''' 방문 길이
https://school.programmers.co.kr/learn/courses/30/lessons/49994

문제 설명
좌표평면 상에서 원점 (0, 0)으로부터 주어진 이동 명령어 UDLR(상하좌우)를 실행했을 때, 지나간 길 중 처음 지나가본 길의 길이를 반환하는 함수 작성
'''

def solution(dirs):
    sets = set()
    y, x = 0, 0
    udrl = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}

    for d in dirs:
        dy, dx = udrl[d]

        # 이동해야하는 좌표
        ny = y + dy
        nx = x + dx

        if -5 <= ny <= 5 and -5 <= nx <= 5:
            sets.add(((y, x), (ny, nx)))  # 현재 위치 -> 이동 후 위치
            sets.add(((ny, nx), (y, x)))  # 이동 후 위치 -> 현재 위치

            y, x = ny, nx  # 이동 위치로 현재 위치 변경

    return len(sets) // 2