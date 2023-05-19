''' 백준 - 주사위 세개
입력
첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

예제 입력 1
3 3 6

예제 출력 1
1300
'''

from collections import Counter

scores = list(map(int, input().split()))

c = Counter(scores)
# print(c)
mode = c.most_common(1)     # 가장 빈도수가 높은 값 찾기
# print(mode) # 최빈도 셋트- [(3, 3)]
# print(mode[0][0])   # 같은 눈
# print(mode[0][1])   # 같은 눈의 갯수

same_mode = mode[0][0]      # 같은 눈
same_mode_cnt = mode[0][1]      # 같은 눈의 갯수

if same_mode_cnt == 3:
    print(10000+same_mode*1000)
elif same_mode_cnt == 2:
    print(1000+same_mode*100)
else:
    print(same_mode*100)

