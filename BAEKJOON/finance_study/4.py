""" [PCCP 모의고사 #2] 2번 - 신입사원 교육
https://school.programmers.co.kr/learn/courses/15009/lessons/121688

아이디어
- 원소 중에 가장 작은 원소 2개 찾기
- 두 원소의 합을 구해서 해당 원소들을 업데이트
"""

ability = [1, 2, 3, 4]
number = 3

for _ in range(number):
    ability.sort()  # 가장 작은 순서대로 나열
    ability[0:2] = sum(ability[0:2]), sum(ability[0:2])

print(sum(ability))