""" 너의 평점은
https://www.acmicpc.net/problem/25206
"""

rating = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0,0]

total = 0   # 학점
result = 0  # 학점 * 등급

for i in range(20):
    subject, r, g = input().split()     #과목명, 학점, 등급

    r = float(r)
    if g != 'P':
        total += r
        result += r * grade[rating.index(g)]

print(round(result/total, 6))