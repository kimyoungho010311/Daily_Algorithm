import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    adj_matrix = [[0] * (N + 1) for _ in range(N + 1)]
    degree = {idx: 0 for idx in range(N + 1)}

    for idx in range(1, N + 1):

        nums = list(map(int, input().split()))

        for num in nums[1:]:
            if num:
                adj_matrix[idx][num] = 1
        degree[idx] = nums[0]

    result = 0

    while degree:

        can_take = [idx for idx, deg in degree.items() if deg == 0]

        if not can_take:
            result = -1
            break
            
        for course in can_take:
            del degree[course]

            for next_course in range(1, N + 1):

                if adj_matrix[next_course][course] == 1:

                    if next_course in degree:
                        degree[next_course] -= 1

        result += 1

    print(f"#{tc} {result}")
