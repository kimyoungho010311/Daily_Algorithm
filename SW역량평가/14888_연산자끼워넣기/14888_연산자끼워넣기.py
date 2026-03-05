import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
'''
N개의 수열이 주어진다. 
N-1 개의 연산자가 주어진다.
주어진 수의 순서를 바꿔서는 안된다.

연산 순서는 무조건 앞에서부터 해야한다.
나눗셈은 정수 나눗셈으로 몫만 취한다.

만약 음수를 양수로 나눌떄는 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꾼다.

최대와 최소를 구해라
'''
from itertools import permutations

# 수의 개수
N = int(input())
arr = list(map(int, input().split()))
# 나중에 연산할거임
# + - * /
operations = list(map(int, input().split()))
opers = []
max_val, min_val = float('-inf'), float('inf')

# 일단 중복되는 연산자가 없는 경우만 고려해본다.
for idx in range(4):
    if idx == 0:
        for _ in range(operations[0]): opers.append('+')
    elif idx == 1:
        for _ in range(operations[1]): opers.append('-')
    elif idx == 2:
        for _ in range(operations[2]): opers.append('*')
    else:
        for _ in range(operations[3]): opers.append('/')
all_opers = set(list(permutations(opers, len(opers))))

for opers in all_opers:
    tmp = arr[0]
    for idx, oper in enumerate(opers):
        if oper == '+':
            tmp += arr[idx+1]
        elif oper == '-':
            tmp -= arr[idx+1]
        elif oper == '*':
            tmp *= arr[idx+1]
        else:
            tmp = int(tmp/arr[idx+1])
        # print(tmp)
    if max_val < tmp:
        max_val = tmp
    if min_val > tmp:
        min_val = tmp

print(max_val)
print(min_val)