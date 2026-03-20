import sys
sys.stdin = open('input.txt')

T = int(input())
MOD = 1000000009
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    W = N - M

    safe_limit = W * (K - 1) + (K - 1)

    if M <= safe_limit:
        print(f"{M % MOD}")
    else:
        # safe_limit을 사용하더라도 뚫리는 경우
        X = M - W * (K - 1)
        groups = X // K

        doubled_score = (pow(2, groups - 1, MOD) - 2) * K

        remains = M - (groups * K)

        result = (doubled_score + remains) % MOD

        print(f"{result}")