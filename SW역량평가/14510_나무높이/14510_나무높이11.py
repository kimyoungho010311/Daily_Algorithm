import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):


    N = int(input())

    trees = list(map(int, input().split()))

    even = odd = 0
    max_h = max(trees)

    for tree in trees:
        h = max_h - tree

        even += h // 2
        odd += h % 2

    while even > odd + 1:
        even -= 1
        odd += 2

    if even == odd:
        ans = even + odd

    elif even > odd:
        ans = even * 2
    else:
        ans = odd * 2 - 1

    print(f"#{tc} {ans}")