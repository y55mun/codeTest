""" 약수들의 합
https://www.acmicpc.net/problem/9506
"""

tmp = []

while 1:
    n = int(input())

    if n == -1:
        break
    else:
        # 모든 약수들을 구하고
        for i in range(1, n):
            if n % i == 0:
                tmp.append(i)

        # 그 약수들의 합 == n => 완전수
        if sum(tmp) == n:
            print(n, '=', ' + '.join(map(str, tmp)))

        else:
            print(n, 'is NOT perfect.')
        tmp = []
