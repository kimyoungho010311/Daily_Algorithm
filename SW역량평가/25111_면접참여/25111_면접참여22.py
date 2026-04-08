import sys
sys.stdin = open('input.txt')
"""

"""

T = int(input())
MOD = 1000000009

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    # 틀린 문제 개수
    W = N - M

    # ㅇ답을 활용해 폭탄을 피할 수 있는 최대 정답 수를 구한다.
    safe_limit = W * (K - 1) + (K + 1)

    if M <= safe_limit:
        print(f"{M % MOD}")
    else: # 만약 M이 safe_limit보다 크다면
        # 오답 방패로 최대한 막아도 어쩔 수 없이 연속으로 붙게 되는 정답의 총 개수 X를 구한다.
        X = M - W * (K - 1)
        # 이 X개가 K씩 묶여서 몇 번의 연석 폭탄을 만드는지 계산한다.
        groups = X // K

        doubled_score = (pow(2, groups + 1, MOD) - 2) * K

        remains = M - (groups * K)

        ans = (doubled_score + remains) % MOD
        print(f"{ans}")


    W = N - M

    safe_limit = W * (K - 1) + (K + 1)

    if M <= safe_limit:
        print(f"{M % MOD}")
    else:

        X = N - W * (K - 1)
        groups = X // K

        doubled_score = (pow(2, groups + 1, MOD) - 2) * K
        remains = M - (groups * K)

        ans = (doubled_score + remains) % MOD






