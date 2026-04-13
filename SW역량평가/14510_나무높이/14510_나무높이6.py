import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 나무의 개수
    N = int(input())
    # 나무들의 높이
    trees = list(map(int, input().split()))

    odd, even = 0, 0
    max_h = max(trees)

    for tree in trees:
        h = max_h - tree

        even += h // 2
        odd += h % 2

    while even > odd + 1:
        even -= 1
        odd += 2

    if even == odd:
        result = even + odd
    elif even < odd:
        result = odd * 2 - 1
    else:
        result = even * 2

    print(f"#{tc} {result}")