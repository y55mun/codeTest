""" 삼각형과 세 변
https://www.acmicpc.net/problem/5073
"""

while True:
    a, b, c = sorted(list(map(int, input().split())))

    if a == b == c == 0:
        break
    # else:
    if a+b <= c:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")