import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    # 나무의 개수
    N = int(input())

    trees = list(map(int, input().split()))

    max_h = max(trees)
    even = odd = 0

    for tree in trees:
        h = max_h - tree
        even += h // 2
        odd += h % 2

    while even > odd + 1:
        even -= 1
        odd += 2

    if even == odd:
        ans = even + odd
    elif even < odd:
        ans = odd * 2 - 1
    else:
        ans = even * 2

    print(f"#{tc} {ans}")
