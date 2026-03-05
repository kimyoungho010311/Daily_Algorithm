import sys
from itertools import permutations
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

# 수의 개수
N = int(input())
arr = list(map(int, input().split()))
operations = list(map(int, input().split()))

oper_list = []
op_symbols = ['+', '-', '*', '/']
for i in range(4):
    for _ in range(operations[i]):
        oper_list.append(op_symbols[i])

max_val = float('-inf')
min_val = float('inf')

# 중복제거를 위해 set 활용
all_opers_comb = set(list(permutations(oper_list, len(oper_list))))

for oper_list in all_opers_comb:
    result = arr[0]
    for idx, oper in enumerate(oper_list):
        if oper == '+':
            result += arr[idx + 1]
        elif oper == '-':
            result -= arr[idx + 1]
        elif oper == '*':
            result *= arr[idx + 1]
        else:
            result = int(result / arr[idx + 1])
    if result > max_val:
        max_val = result
    if result < min_val:
        min_val = result

print(max_val)
print(min_val)