'''
대표값

N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높
은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

▣ 입력설명
첫줄에 자연수 N(5_문자열<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연
수가 주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
평균은 소수 첫째 자리에서 반올림합니다.

▣ 입력예제 1
10
45 73 66 87 92 67 75 79 75 80

▣ 출력예제 1
74 7

'''
import math

n = int(input())
scores = list(map(int, input().split()))

avg = round(sum(scores) / n)

min = 2147000000    # int 4바이트에서 가장 큰 수

for idx, x in enumerate(scores):
    tmp = abs(x - avg)  # (학생점수 - 평균) 의 절대값. 학생점수와 평균과의 거리

    # |학생 점수 - 평균|의 최소값 구하기 = 평균과 가장 가까운 값
    if tmp < min:
        min = tmp
        score = x   # 학생 점수 최소값 저장할 변수
        res = idx + 1   # 인덱스 저장

    # 평균과 가장 가까운 값 중에서 73, 75의 경우 둘 다 평균값인 74와 거리가 1이므로 이를 판별해줘야함
    elif tmp == min:
        if x > score:    # 학생점수 최대값 구하기 : 75 > 73
            score = x   # 학생점수 최대값 75 저장
            res = idx + 1   # 학생점수 최대값 인덱스

print(avg, res)