"""
https://leetcode.com/problems/valid-parentheses/description/
"""

s = input()


stack = []
for p in s:
    if p == '{':
        stack.append("}")
    elif p == '[':
        stack.append("]")
    elif p == '(':
        stack.append(")")
    elif stack and stack[-1] == p:
        stack.pop()
    else:
        print("False")
