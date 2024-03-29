""" 크로스 컨트리
https://www.acmicpc.net/problem/9017

아이디어
1. 팀 별 주자수 세기
2. 제외되는 팀 구하기
3. 점수 계산
"""

t = int(input())

for _ in range(t):
    n = int(input())
    temp = list(map(int, input().split()))
    count = {}  # 팀 별 주자수

    # 1. 팀 별로 주자수 세기
    for i in range(n):
        if temp[i] in count:
            count[temp[i]] += 1
        else:
            count[temp[i]] = 1

    # 2. 제외되는 팀 구하기
    dele = {}
    for k,v in count.items():
        if v < 6:
            dele[k] = 1

    # 3. 점수 계산
    team = {}   # 팀, 팀 별 점수
    score = 1   # 점수
    for i in range(n):
        if temp[i] not in dele: # 제외되는 팀이 아닐 경우에만 점수 계산 가능
            if temp[i] in team:
                if team[temp[i]][0] < 4:
                    team[temp[i]][0] += 1
                    team[temp[i]][1] += score
                elif team[temp[i]][0] == 4:
                    team[temp[i]][0] += 1
                    team[temp[i]][2] = score
            else:
                team[temp[i]] = [1, score, 0]   # [팀 당 주자 수, 상위 4명의 합, 5번째 주자 점수]
            score += 1


    team = sorted(team.items(), key = lambda x:(x[1][1], x[1][2]))
    print(team[0][0])