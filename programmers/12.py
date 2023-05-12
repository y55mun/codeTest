'''
softeer - 지도 자동 구축

자율주행차용 정밀 지도에 관한 궁금증으로 인터넷 검색을 해보니, Diamond-Square-Algorithm이라는 것을 찾게 되었다.
이 알고리즘은 정사각형을 이루는 점 4개를 고르고 그 후에는 다음과 같은 과정을 거쳐 모양이 만들어진다.
정사각형의 각 변의 중앙에 점을 하나 추가한다. 정사각형의 중심에 점을 하나 추가한다.

입력형식
첫째 줄에 N이 주어진다.

출력형식
첫째 줄에 N단계를 거친 점의 개수를 출력한다.

입력예제1
1

출력예제1
9

'''

import sys
input = sys.stdin.readline

n = int(input())
result = (n+2)*(n+2)

print(result)