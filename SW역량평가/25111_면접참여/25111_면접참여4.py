import sys
sys.stdin = open('input.txt')

T = int(input())
MOD = 1000000009

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    W = N - M # 틀린 문제 개수

    safe_limit = W * (K - 1) + (K - 1)

    if M <= safe_limit:
        print(f"{M % MOD}")
    else:
        X = M - W * (K - 1)
        g = X // K

        double_score = (pow(2, g + 1, MOD) - 2) * K

        remains = M - (g * K)

        ans = (double_score + remains) % MOD
        print(f"{ans}")



    W = N - M
    safe = W * (K - 1) + (K - 1)

    if M <= safe:
        print(f"{M % MOD}")

    else:

        X = M - W * (K - 1)
        g = X // K

        double = (pow(2, g + 1, MOD) - 2) * K

        r = M - (g * K)

        ans = (double + r) % MOD
        print(ans)