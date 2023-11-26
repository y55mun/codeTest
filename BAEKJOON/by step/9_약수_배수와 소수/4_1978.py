""" 소수 찾기
https://www.acmicpc.net/problem/1978
"""

n = int(input())
a = list(map(int, input().split()))

ans = 0

"""
a에 있는 원소가 소수인지 판별
그 갯수를 count
"""
for num in a:
    if num > 1:
        # 소수 판별
        for j in range(2, num+1):   # 1은 소수가 아니니 제외
            if num % j == 0:
                if num == j:
                    ans += 1
                break       # num에 도달하지 못하고 중간에 나누어떨어지는 수를 만나게 되면 해당 수는 소수가 아님
print(ans)