import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cur_sum = sum(A[:K])
    windows = [cur_sum]

    for i in range(1, N - K + 1):
        cur_sum += A[i + K - 1] - A[i - 1]
        windows.append(cur_sum)

    max_left = -float('inf')
    ans = -float('inf')

    for i in range(1, len(windows)):

        max_left = max(max_left, windows[i - K])
        ans = max(ans, max_left + windows[i])

    print(f"#{tc} {ans}")