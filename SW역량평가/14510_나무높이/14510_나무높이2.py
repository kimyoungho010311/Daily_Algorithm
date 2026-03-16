import sys
sys.stdin = open('input.txt')
"""


"""

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_h = max(trees)
    even, odd = 0, 0

    for tree in trees:
        h = max_h - tree
        even += h // 2
        odd += h % 2

    while even > odd + 1:
        even -= 1
        odd += 2

    if odd == even:
        result = odd + even
    elif odd < even:
        result = even * 2
    else:
        result = odd * 2 - 1

    print(f"#{tc} {result}")