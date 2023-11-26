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
        for j in range(2, num+1):
            if num % j == 0:
                if num == j:
                    ans += 1
                break
print(ans)