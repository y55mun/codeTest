'''올바른 괄호
https://school.programmers.co.kr/learn/courses/30/lessons/12909

문제 설명
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

입출력 예
s	answer
"()()"	true
"(())()"	true
")()("	false
"(()("	false

'''

def solution(s):
    stack = []

    for i in s:
        if i == '(':    # 왼쪽 괄호가 나오면 스택에 추가
            stack.append(i)
        else:
            if stack == []: # 오른쪽 괄호로 시작할경우
                return False
            else:   # 오른쪽 괄호가 나오면 스택에서 pop
                stack.pop()

    if stack != []:     # 다 끝났는데 왼쪽 괄호가 스택에 남아있을경우
        return False
    return True