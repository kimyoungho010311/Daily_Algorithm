import sys
sys.stdin = open('inpurt.txt')
from itertools import permutations
"""
카트를 들고 각 관리구역을 돌고 다시 돌아와야 한다.
최소 배터리 사용량(최소 비용)을 다뤄야 한다.
"""
T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 사무실(0번)을 뺀 나머지 관리구역 리스트 생성 (1 ~ N-1)
    delivery_area = [i for i in range(1, N)]

    # 관리구역들만 순서를 섞음
    perms = list(permutations(delivery_area))
    # print(perms)
    data = [list(map(int, input().split())) for _ in range(N)]

    min_battery = float('inf')

    # 생성된 순열 앞뒤로 0을 붙여서 경로 완성
    for p in perms:
        path = (0,) + p + (0,)

        current_sum = 0
        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]
            current_sum += data[start][end]

        if current_sum < min_battery:
            min_battery = current_sum

    print(f"#{tc} {min_battery}")