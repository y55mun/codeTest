""" 삼각형 외우기
https://www.acmicpc.net/problem/10101
"""

angle = []

for i in range(3):
    angle.append(int(input()))

if angle.count(60) == 3:
    print("Equilateral")
elif sum(angle) == 180:
    if len(set(angle)) == 2:
        print("Isosceles")
    else:
        print("Scalene")
elif sum(angle) != 180:
    print("Error")

