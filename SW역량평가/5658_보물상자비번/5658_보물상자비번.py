import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    nums = deque(input().strip())

    group_size = N // 4
    ans_set = set()

    for _ in range(group_size):
        # 현재 상태에서 4개 변의 숫자 추출
        for i in range(0, N, group_size):
            # 큐를 리스트로 바꿔서 필요한 만큼만 join
            hex_str = "".join(list(nums)[i : i + group_size])
            ans_set.add(hex_str)

        nums.rotate(1)

    result = sorted([int(x, 16) for x in ans_set], reverse=True)

    print(f"#{tc} {result[K-1]}")


