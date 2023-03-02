"""후위식 연산
후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 21입니다.

▣ 입력설명
첫 줄에 후위연산식이 주어집니다. 연산식의 길이는 50을 넘지 않습니다.
식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.

▣ 출력설명
연산한 결과를 출력합니다.

▣ 입력예제 1
352+*9-

▣ 출력예제 1
12
"""

a = input()
stack = []
ans = ''

for x in a:
    # if x.isdecimal():   # 10진수 인지 확인 후
    #     ans += x    # 저장
    #
    # # 연산자 일 경우 +-*/()
    # else:
        # if x == '(':
        #     stack.pop(x)
        #
        # elif x == ')':
        #     while stack and stack[-1] != '(':   # (를 만날 때까지 연산
        #         ans += stack.append()
        #     stack.append()     # 스택에 쌓여있는 ( 없애기
    if x.isdecimal():
        stack.append(int(x))
        else:  # 연산자 일 경우
        if x == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 + n1)
        elif x == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 - n1)
        elif x == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
        elif x == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 / n1)

print(stack)