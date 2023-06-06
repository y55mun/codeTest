'''
softeer - 금고털이

입력형식
첫 번째 줄에 배낭의 무게 W와 귀금속의 종류 N이 주어진다. i + 1 (1 ≤ i ≤ N)번째 줄에는 i번째 금속의 무게 Mi와 무게당 가격 Pi가 주어진다.

출력형식
첫 번째 줄에 배낭에 담을 수 있는 가장 비싼 가격을 출력하라.

입력예제1
100 2
90 1
70 2

출력예제1
170

'''

import sys
input = sys.stdin.readline

w, n = map(int, input().split())

result = 0

mpDic = {}
for i in range(n):
    m, p = map(int, input().split())
    mpDic[m] = p

maxP = max(mpDic.values())  # 가장 비싼 금속의 가격

maxP_of_M = 0   # 가장 비싼 금속의 무게
# 가장 비싼 금속의 무게 찾기
for m, p in list(mpDic.items()):
    if p == maxP:
        maxP_of_M = m

    # 금속의 무게와 배낭의 무게 비교
    if maxP_of_M < w:
        result = (maxP_of_M * maxP) + (w -  maxP_of_M)
    elif maxP_of_M == w:
        result = maxP_of_M * maxP
    else:
        del mpDic[maxP_of_M]
        # print(mpDic)
        maxP_of_M = max(mpDic.values())
        maxP = max(mpDic.values())
        result = (maxP_of_M * maxP) + (w -  maxP_of_M)

print(result)

