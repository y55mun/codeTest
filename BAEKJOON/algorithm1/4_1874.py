""" 스택 수열
https://www.acmicpc.net/problem/1874
"""

n = int(input())
stack, ans, find = [], [], True

now = 1
for _ in range(n):
    num = int(input())

    # num 이하 숫자까지 스택에 넣기
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1
    # num 이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        ans.append('-')

    # 스택 수열을 만들 수 없으므로 False
    else:
        find = False

# 스택 수열을 만들수 있는지 여부에 따라 출력
if not find:
    print('NO')
else:
    for i in ans:
        print(i)