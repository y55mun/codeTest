"""바구니 뒤집기
https://www.acmicpc.net/problem/10811
"""

N, M = map(int, input().split())
basket = list(range(1, N+1))    # 바구니에 번호 입력

for _ in range(M):
    i, j = map(int, input().split())

    # i번째 ~ j번째 바구니의 순서를 역순으로 변경
    basket = basket[0:i-1] + list(reversed(basket[i-1:j])) + basket[j:]
#     basket = basket[1:i+1] + list(reversed(basket[i+1:j])) + basket[j:]
for i in basket:
    print(i, end=' ')