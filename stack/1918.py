import sys

s = sys.stdin.readline().strip()
stack = []
result = ''

priority = {'+':1, '-':1, '*':2, '/':2}

for ch in s:
    if ch.isalpha():
        result += ch
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    else:
        while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[ch]:
            result += stack.pop()
        stack.append(ch)

while stack:
    result += stack.pop()

print(result)