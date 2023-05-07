'''
공원 산책
'''

def solution(park, routes):
    # 시작 위치 찾기
    for j in range(len(park)):
        for i in range(len(park[j])):
            if park[j][i] == "S":
                sj = j
                si = i

    for route in routes:
        a = sj
        b = si
        for step in range(int(route[2])):

            # 북: 현재 위치가 map 가장 위쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            if route[0] == "N" and a != 0 and park[a - 1][b] != 'X':  # 북
                a -= 1
                if step == int(route[2]) - 1:
                    sj = a
            elif route[0] == "S" and a != len(park) - 1 and park[a + 1][b] != 'X':  # 남
                a += 1
                if step == int(route[2]) - 1:
                    sj = a
            elif route[0] == "W" and b != 0 and park[a][b - 1] != 'X':  # 서
                b -= 1
                if step == int(route[2]) - 1:
                    si = b
            elif route[0] == "E" and b != len(park[0]) - 1 and park[a][b + 1] != 'X':  # 동
                b += 1
                if step == int(route[2]) - 1:
                    si = b
    return [sj, si]