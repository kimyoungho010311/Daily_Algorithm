import sys
sys.stdin = open('input.txt')

T = int(input())
MOD = 1000000009

for tc in range(1, T+1):
    # 총 문제, 맞힌 문제, 연속 기준
    N, M, K = map(int, input().split())

    # 틀린 문제
    W = N - M

    safe_limit = W * (K - 1) + (K - 1)

    if M <= safe_limit:
        print(f"{M % MOD}")
    else:
        # 어쩔 수 없이 연속으로 붙게 되는 정답의 총 개수 X
        X = M - W * (K - 1)

        # 이 X가 K개씩 묶여서 몇 번의 연속 두배이벤트를 만드는지 계산한다.
        groups = X // K

        doubled_score = (pow(2, groups + 1, MOD) - 2 ) * K

        remains = M - (groups * K)

        print(f"{(doubled_score + remains) % MOD}")


        