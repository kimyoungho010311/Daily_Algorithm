# import sys
# sys.stdin = open('input.txt')
'''
정수 X에 사용할 연산은 다음 세 가지다.
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면 2로 나눈다.
3. 1을 뺸다.

정수 N이 주어질 때, 위 연산을 적용해서 1로 만들려고 한다. 연산을 사용하는 최솟값을 출력해라

1.5초만에 해야함
'''

N = int(input())

keep_going = True
cnt = 0

while keep_going:
    if N == 1:
        keep_going = False

    if N % 3 == 0:
        cnt += 1
        N //= 3
        if N == 1:
            keep_going = False
    elif N % 2 == 0:
        cnt += 1
        N //= 2
        if N == 1:
            keep_going = False
    else:
        N -= 1
        cnt += 1
        if N == 1:
            keep_going = False

print(cnt)