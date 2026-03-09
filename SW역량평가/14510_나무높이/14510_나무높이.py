import sys
sys.stdin = open('input.txt')

T = int(input())
T = 10

# 뭔가 물 안주는 날 정하는게 첫쩃날 둘쨋날만 고려하면 될듯

def water_trees(start_day, copy_trees_height):
    while True:

        # 가장 작은 나무를 찾고
        min_tree = min(copy_trees_height)

        if min_tree == max_tree:
            break

        # 짝수 홀수에 따라 다른 높이가 커지도록 한다.
        if start_day // 2 == 0:
            is_odd = False
        elif start_day // 2 != 0:
            is_odd = True

        if is_odd: # 홀수이면
            copy_trees_height[copy_trees_height.index(min_tree)] += 1
        if not is_odd:
            copy_trees_height[copy_trees_height.index(min_tree)] += 2

        start_day += 1
    return start_day

for tc in range(1, T+1):
    # 나무의 개수
    N = int(input())
    # 나무들의 높이
    trees_height = list(map(int, input().split()))
    copy_trees_height = trees_height[:]

    # 가장 큰 나무를 목표로 설정한다.
    max_tree = max(trees_height)
    # print(trees_height)
    is_odd = True
    min_day, start_day = float('inf'), 0

    # 일단 while문으로 시작해보고
    # 중간에 break 로직을 구해본다.
    # 백트래킹?
    start_day = water_trees(start_day, copy_trees_height)

    if min_day > start_day:
        min_day = start_day
    print(f"first min day: {min_day}")
    # 여기서 이제 첫 쨋날은 물 안주는걸로 해본다.
    copy_trees_height = trees_height[:]
    start_day = 1
    start_day = water_trees(start_day, copy_trees_height)

    if min_day > start_day:
        min_day = start_day
    print(f"second min day: {min_day}")

    # print(trees_height)
    print(f"#{tc} {min_day}")