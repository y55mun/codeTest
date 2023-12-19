""" 삼각형과 세 변
https://www.acmicpc.net/problem/5073
"""
triangle = []
maxx = 0

while True:
    triangle = list(map(int, input().split()))
    # print(max(triangle))
    print(triangle)
    maxx = max(triangle)
    print(maxx)
    print(triangle.remove(7))

    if triangle == 0:
        break
    # if max(triangle) >= sum(triangle.remove(max(triangle))): # 삼각형의 조건을 만족하지 못한 경우. remove 함수 몰랐었음!!!
    #     print("Invalid")
    # else:
    #     if len(list(set(triangle))) == 1:
    #         print("Equilateral")
    #     elif len(list(set(triangle))) == 2:
    #         print("Isosceles")
    #     else:
    #         print("Scalene")


    # if a == 0 and b == 0 and c== 0:
    #     break
    # else:
    #     max = a
    #
    #
    #     if
    #
    #     if a == b == c:
    #         print("Equilateral")
    #     elif a != b != c:
    #         print("Scalene")
    #     else:
    #         print("Isosceles")