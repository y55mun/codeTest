""" 쇠막대기
https://www.acmicpc.net/problem/10799
"""

ir = input()
stack = []
cnt = 0

for i in range(len(ir)):
    if ir[i] == '(':
        stack.append("(")
    else:      # ')' 가 나올 2가지 경우
        if ir[i-1] == "(":  # 이전이 '(' 이면 '('를 pop 하고 현재 스택에 있는 '(' 수 만큼 더하기
            stack.pop()
            cnt += len(stack)

        else:   # 그 외 나머지 부분 카운ㅌ
            stack.pop()
            cnt += 1

print(cnt)