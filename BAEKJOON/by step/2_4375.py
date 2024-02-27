""" 1
https://www.acmicpc.net/problem/4375
"""

while True:
    try:
        n = int(input())
    except:
        break

    num = 1
    num_count = 1   # 자리수

    while True:
        if num % n != 0:    # n의 배수일 경우
            num = num*10 + 1    # 1로만 이루어진 다음 수로 갱신
            num_count += 1  # 자리수 카운트
        else:   # n의 배수가 아닐 경우 종료
            break
    print(num_count)

