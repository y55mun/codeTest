"""공 바꾸기
https://www.acmicpc.net/problem/10813
"""

N, M = map(int, input().split())
# basket = [0] * (N+1)
basket = [range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())

    # i번 바구니와 j번 바구니 교환
    basket[i], basket[j] = basket[j], basket[i]

# for i in range(1, N+1):
#     print(basket[i], end=' ')
print(basket[1:])