""" 진법 변환
https://www.acmicpc.net/problem/2745
"""

# N, B = input().split()
#
# print(int(N, int(B)))

def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

print(solution(int('c',16),4))  # 16진수인 C를 4진수로 바꾸는것
print(solution(int('4',6),3))  # 6진수인 4를 3진수로 바꾸는것
print(solution(int('21',3),7)) # 3진수인 21을 7진수로 바꾸는것
print(solution(int('15',9),5)) # 9진수인 15를 5진수로 바꾸는것