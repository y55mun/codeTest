""" 단어 뒤집기 2
https://www.acmicpc.net/problem/17413

아이디어
1. 문제 확인해보면 문자열을 단순히 전부 다 뒤집어서 출력하는 것이 아니다!!
2. 문자를 뒤집어서 출력하는 방법 -> stack 이용!!
3. <와 > 사이에 있는 문자들은 뒤집으면 안된다. 그러면 괄호 안에 있다는 것을 정의해줄 방법이 필요.
"괄호 안에 존재하는 문자열은 스택의 첫번째 부터 pop 하여 순차적으로 정답에 추가"
4. < 를 만나기 전에 있던 문자들은 stack 을 뒤집어서 출력 후 비워줘야 출력시에 <랑 같이 뒤집어 지는 불상사가 발생하지 않는다.
=> <를 만나면 전부 털고, 괄호 안에 있다는 표시 check = True 로 한다.
5. > 를 만나면 괄호 빠져 나옴을 표시해주고, stack 안에 있는 애들을 뒤집지 말고 정직하게 출력.

" 괄호 밖에 존재하는 문자열은 스택의 마지막부터 pop 하여 역순차적으로 정답에 추가"
6. 공백을 만날때마다 출력해주는 형식이니 공백을 만나고 괄호 밖에 있다면 result 에 하나씩 역으로 더해주고 최종적으로 출력.
"""

stack = []
result = ''
check = False  # 괄호가 있는지 체크

data = input()

for i in data:
    # 스택에 존재하는 값을 역으로 추가
    if i == '<':
        check = True
        for _ in range(len(stack)):
            result += stack.pop()   # 마지막 요소 꺼내기
    stack.append(i)

    # 스택에 존재하는 값은 괄호안의 값이기에 순차적으로 추가
    if i == '>':
        check = False
        for _ in range(len(stack)):
            result += stack.pop(0)

    # 스택에 존재하는 값을 역으로 추가
    if i == ' ' and check == False:
        for k in range(len(stack)):
            if k == 0:
                stack.pop()
                continue
            result += stack.pop()
        result += ' '

if stack:
    for _ in range(len(stack)):
        result += stack.pop()

print(result)