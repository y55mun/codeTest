"""공 바꾸기
https://www.acmicpc.net/problem/10813
"""

N, M = map(int, input().split())
basket = list(range(1, N+1))

for i in range(M):
    i, j = map(int, input().split())

    # i번 바구니와 j번 바구니 교환
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for i in range(N):
    print(basket[i], end=' ')