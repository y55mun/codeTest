""" 완전탐색
모의고사
https://school.programmers.co.kr/learn/courses/30/lessons/42840

"""


def solution(answers):
    answer = []

    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == s1[i % 5]:
            score[0] += 1
        if answers[i] == s2[i % 8]:
            score[1] += 1
        if answers[i] == s3[i % 10]:
            score[2] += 1

    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i + 1)

    return sorted(answer)