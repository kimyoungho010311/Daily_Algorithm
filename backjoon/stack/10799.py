import sys

l = list(sys.stdin.readline().strip())
stack = []
cnt = 0

for i in range(len(l)):
    if l[i] == '(':
        # 다음이 ')'이면 레이저
        if i + 1 < len(l) and l[i+1] == ')':
            cnt += len(stack)
        else:
            stack.append('(')
    else:  # ')'
        if i > 0 and l[i-1] != '(':  # 막대 끝
            cnt += 1
            stack.pop()  # 막대 끝이므로 스택에서 제거

print(cnt)