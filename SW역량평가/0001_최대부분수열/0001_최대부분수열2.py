import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # [1단계] 길이 K인 모든 윈도우(부분 배열)의 합을 미리 구해두기
    cur_sum = sum(A[:K])
    windows = [cur_sum]

    for i in range(1, N - K + 1):
        cur_sum += A[i + K - 1] - A[i - 1]  # 새 원소 더하고, 옛날 원소 빼기
        windows.append(cur_sum)

    # [2단계] 겹치지 않는 두 윈도우의 최대합 찾기
    max_left = -float('inf')
    ans = -float('inf')

    for i in range(K, len(windows)):
        # 현재 윈도우(i)와 겹치지 않는 왼쪽 윈도우(i-K) 중 최댓값 갱신
        max_left = max(max_left, windows[i - K])
        # (왼쪽 최댓값 + 현재 윈도우 합)으로 전체 최댓값 갱신
        ans = max(ans, max_left + windows[i])

    print(f"#{tc} {ans}")