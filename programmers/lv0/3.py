'''더 크게 합치기
https://school.programmers.co.kr/learn/courses/30/lessons/181939

'''
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))