"""카드 역배치(정올 기출)

오름차순으로 한 줄로 놓여있는 20장의 카드에 대해 10개의 구간이 주어지면, 주어진 구간의 순서대로 위의 규칙에 따라 순서를 뒤집는 작업을 연속해서 처리한 뒤
마지막 카드들의 배치를 구하는 프로그램을 작성하시오.

▣ 입력설명
총 10개의 줄에 걸쳐 한 줄에 하나씩 10개의 구간이 주어진다. i번째 줄에는 i번째 구간의 시
작 위치 ai와 끝 위치 bi가 차례대로 주어진다. 이때 두 값의 범위는 1 ≤ ai ≤ bi ≤ 20이다.

▣ 출력설명
1부터 20까지 오름차순으로 놓인 카드들에 대해, 입력으로 주어진 10개의 구간 순서대로 뒤집
는 작업을 했을 때 마지막 카드들의 배치를 한 줄에 출력한다.

▣ 입력예제 1
5_문자열 10
9 13
1 2
3 4
5_문자열 6
1 2
3 4
5_문자열 6
1 20
1 20

▣ 출력예제 1
1 2 3 4 10 9 8 7 13 12 11 5_문자열 6 14 15 16 17 18 19 20
"""

import sys
cards = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())

    for j in range((e-s+1)//2):
        cards[s+j], cards[e-j] = cards[e-j], cards[s+j]
cards.pop(0)

for x in cards:
    print(x, end=' ')