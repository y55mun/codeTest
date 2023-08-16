""" 단어변환
https://school.programmers.co.kr/learn/courses/30/lessons/43163
"""

"""
1. 아이디어
- 최소 단계를 찾아야 하므로 bfs

"""


from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0

    q = deque()
    q.append([begin, 0])  # 시작단어와 깊이를 넣어준다.

    while q:
        x, cnt = q.popleft()  # 단어, 이동한 횟수

        if x == target:
            return cnt

        for i in range(len(words)):
            diff = 0
            word = words[i]

            for j in range(len(x)):
                if x[j] != word[j]:
                    diff += 1
            if diff == 1:
                q.append([word, cnt + 1])

    return answer