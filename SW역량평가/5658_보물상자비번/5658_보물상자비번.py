
"""
0 1 2 3 4 5 6 7 8 9 A B C D E F

뚜겅은 시계방향으로 돌릴 수 있고, 한 번 돌릴 때마다 숫자가 시계방향으로 한 칸씩 회전한다.

int(16진수문자열, 16)
중복되는게 생길 수 있으니깐 set으로 한 다음에 정렬하자.

2차원 리스트로 pop push 하면 편할 듯?
-> 아니다 리스트 4개 만들고 큐로 하면 될듯..?
"""
import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
# T = 1
for tc in range(1, T+1):
    # 숫자 수, 번재 큰 수
    N, K = map(int, input().split())
    nums = list(map(str, input().strip()))

    n = len(nums)
    group_size = n // 4
    groups = []

    for idx, i in enumerate(range(0, n, group_size)):
        # [['1', 'B', '3'], ['B', '3', 'B'], ['8', '1', 'F'], ['7', '5', 'E']]
        groups.append(nums[i : i + group_size]) #

    q0 = deque(groups[0])
    q1 = deque(groups[1])
    q2 = deque(groups[2])
    q3 = deque(groups[3])

    ans = []
    # print(f"Before: {q0}, {q1}, {q2}, {q3}")
    for i in range(4):
        # tmp = q0.pop()
        q1.insert(0, q0.pop())
        # tmp = q1.pop()
        q2.insert(0, q1.pop())
        # tmp = q2.pop()
        q3.insert(0, q2.pop())
        # tmp = q3.pop()
        q0.insert(0, q3.pop())

        # print(f"{list(q0)}, {list(q1)}, {list(q2)}, {list(q3)}")
        qs = [q0, q1, q2, q3]
        # [deque(['E', '1', 'B']), deque(['3', 'B', '3']), deque(['B', '8', '1']), deque(['F', '7', '5'])]
        # [deque(['5', 'E', '1']), deque(['B', '3', 'B']), deque(['3', 'B', '8']), deque(['1', 'F', '7'])]
        # [deque(['7', '5', 'E']), deque(['1', 'B', '3']), deque(['B', '3', 'B']), deque(['8', '1', 'F'])]

        for q in qs:
            tmp = ''
            for elem in q:
                tmp += elem
            if tmp not in ans:
                ans.append(tmp)
    # print(ans)
    final = []
    for elem in ans:
        final.append(int(elem, 16))

    final.sort(reverse=True)
    # print(final)
    print(f"#{tc} {final[K-1]}")


"""
F535/86D7/6286/B2D8

"""
























