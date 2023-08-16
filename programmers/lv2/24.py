""" 단어변환
https://school.programmers.co.kr/learn/courses/30/lessons/43163
"""

"""
1. 아이디어
- 최소 단계를 찾아야 하므로 bfs

"""

from collections import deque

def solution(begin, target, words):
    if target not in words:  # 애초에 words리스트에 target값이 없다면 return 0
        return 0

    answer = 0

    q = deque()
    q.append([begin, 0])  # 시작단어와 깊이를 넣어준다.

    while q:
        x, cnt = q.popleft()  # 단어, 이동한 횟수

        if x == target:
            return cnt

        # 단어를 모두 체크하면서, 해당 단어가 변경될 수 있는지 체크
        for i in range(len(words)):
            diff = 0  # 다른 글자의 갯수
            word = words[i]

            for j in range(len(x)):  # 단어의 길이만큼 반복
                if x[j] != word[j]:  # 단어에 알파벳 한개씩 체크하기
                    diff += 1
            if diff == 1:
                q.append([word, cnt + 1])

    return answer