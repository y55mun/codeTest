'''카펫
https://school.programmers.co.kr/learn/courses/30/lessons/42842
'''


def solution(brown, yellow):
    answer = []

    div = []
    # 약수(div) 구하기
    for i in range(1, (brown + yellow) + 1):
        if (brown + yellow) % i == 0:
            div.append(i)

    w = 0
    h = 0

    for i in div:
        w = i
        h = (brown + yellow) // w

        if w >= h:
            if brown == 2 * w + 2 * h - 4:
                return [w, h]