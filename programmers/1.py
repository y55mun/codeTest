""" [PCCP 모의고사 #1] 1번 - 외톨이 알파벳
https://school.programmers.co.kr/learn/courses/15008/lessons/121683?language=python3
"""

import collections

ans = []

input_string = input()
input_str = collections.Counter(input_string)   # 글자수 카운팅
# Counter({'a': 3, 'e': 2, 'd': 2, 'b': 2, 'c': 2})

for k,v in input_str.items():
    if v > 1:
        index = input_string.index(k)   # 각 글자수의 index 찾기
        input_str2 = collections.Counter(input_string[index:index+v])
        if len(input_str2) >= 2:
            ans.append(k)

if len(ans) == 0:
    print("N")

ans = ''.join(sorted(ans))
print(ans)
