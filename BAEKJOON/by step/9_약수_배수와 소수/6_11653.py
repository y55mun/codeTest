""" 소인수분해
https://www.acmicpc.net/problem/11653
"""

n = int(input())
cnt = 0
ans = []
for i in range(2, n):
    count = 0   # 약수의 갯수

    if n % i == 0:
        count += 1

        for j in range(2, i):
            if j % i == 0:
                count += 2
                break
        if count == 1:
            n //= i
            ans.append(i)


print(ans)
