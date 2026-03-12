import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B = map(int, input().split())
count = 1

# 반대로 B -> A 로 가는 연산을 해본다.
# 거꾸로 연산중에 만약 1이 있다면 -1 % 10 을 해준다.
# 1이 없다면 // 2를 해준다.

# 만약 위에 1이 없고 홀수인 경우에는 -1을 출력한다.

# 무한 반복중에 curr_num이 0이 되면 종료하고 count를 반환한다.

while B > A:
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    else:
        print(-1)
        exit()
    count += 1

print(count if B == A else -1)
