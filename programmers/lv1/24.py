""" 완전탐색
모의고사
https://school.programmers.co.kr/learn/courses/30/lessons/42840

"""

def solution(answers):
    answer = []
    score = [0, 0, 0]

    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 학생 별 정답과 비교 후 정답 갯수 카운트
    for i in range(len(answers)):
        if answers[i] == student1[i % 5]:
            score[0] += 1
        if answers[i] == student2[i % 8]:
            score[1] += 1
        if answers[i] == student3[i % 10]:
            score[2] += 1

    # enumerate 함수를 이용해 점수에 해당하는 인덱스, 즉, 학생 구하기
    for idx, num in enumerate(score):
        if num == max(score):
            answer.append(idx + 1)

    return answer