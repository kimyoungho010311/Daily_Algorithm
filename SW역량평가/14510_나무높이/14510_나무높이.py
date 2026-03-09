import sys
sys.stdin = open('input.txt')
"""
핵심로직은 며칠이 걸릴까?가 아닌 1이 총 몇개 필요하고 2가 총 몇개 필요한가? 이다.
그리고 그 두 수의 균형을 맞추는게 핵심이다.
"""
T = int(input())

for tc in range(1, T+1):
    # 나무의 수
    N = int(input())
    trees = list(map(int, input().split()))

    odd, even = 0, 0

    max_h = max(trees)
    # 각 나무에 대해 max_h - h 를 계산한다.
    for tree in trees:
        # 각 나무마다 얼만큼 성장이 필요한지 계산
        # 만약 1 -> 7가 되기 위해서는 2, 2, 2, 1 이 필요함
        h = max_h - tree
        even += h // 2
        odd += h % 2

    # 핵심 로직인 두 수의 균형을 맞추기
    # 만약 짝수날이 너무 많으면 필연적으로 쉬는날(홀수)가 많아진다.
    # 그러면 전체 일수가 줄어듬으로 최대한 많이 짝수를 홀수로 나눈다!
    while even > odd + 1: # 멈추는 순간이 바로 even > odd + 1인 순간
        even -= 1
        odd += 2
        # 왜 +1인가?
        # -> odd와 even이 같거나, odd가 1개 더 많은 게 최적이기 때문!

    if odd == even:
        result = odd + even
    elif odd > even: # 1이 더 많음
        result = odd * 2 - 1
    else: # odd < even # 2가 더 많음
        result = even * 2

    print(f"#{tc} {result}")