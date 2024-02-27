""" 1
https://www.acmicpc.net/problem/4375
"""

while True:
    try:
        n = int(input())
    except:
        break

    num = 1
    num_count = 1

    while True:
        if num % n != 0:
            num = num*10 + 1
            num_count += 1
        else:
            break
    print(num_count)

