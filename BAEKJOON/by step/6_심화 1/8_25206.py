""" 너의 평점은
https://www.acmicpc.net/problem/25206
"""

rating = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0,0]

total = 0   # 학점
result = 0  # (학점 * 등급) 총합을 담은 변수

for i in range(20):
    subject, r, g = input().split()     #과목명, 학점, 등급

    r = float(r)    # str 로 인식해서 오류 발생해서 float 형으로 변경 해줌
    if g != 'P':    # 등급이 'P'인 과목은 계산 안함
        total += r
        result += r * grade[rating.index(g)]

print(round(result/total, 6))