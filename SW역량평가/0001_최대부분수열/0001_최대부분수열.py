import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    sub_sums = []
    current_sum = sum(arr[:K])
    sub_sums.append(current_sum)

    for i in range(1, N - K + 1):
        current_sum = current_sum - arr[i - 1] + arr[i + K - 1]
        sub_sums.append(current_sum)

    M = len(sub_sums)

    left_max = [0] * M
    left_max[0] = sub_sums[0]
    for i in range(1, M):
        left_max[i] = max(left_max[i - 1], sub_sums[i])

    right_max = [0] * M
    right_max[M - 1] = sub_sums[M - 1]
    for i in range(M - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], sub_sums[i])

    ans = -float('inf')
    for i in range(M - K):
        ans = max(ans, sub_sums[i] + right_max[i + K])

    print(f"#{tc} {ans}")