import sys
sys.stdin = open('input.txt')
"""
네트워크와 시작점이 주어질때, 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구해라

방향이 있는 그래프이다.

흠.. BFS를 하면서 깊이도 같이 구한다.
깊이에 따라서 해당 인덱스를 []애 넣고 깊이 들어갈 때마다 해당 깊이의 인덱스의 값을 넣는다?

연락 인원은 총 100명이다.
최악의 경우 1 ~ 100번째 사람까지 총 100번이 걸릴 수 있으니깐 총 길이 100만큼의 리스트를 구해놓는다

call_order = [[], [], [], [], [], ... ,[]]

인접리스트로 만들면 간단할듯
"""
from collections import deque

T = 10

def BFS(start):
    q = deque([(start, 0)])
    visited[start] = True

    # max_depth = 0

    while q:
        curr, depth = q.popleft()

        # 현재 깊이 정보를 업데이트
        # max_depth = max(max_depth, depth)
        # 해당 깊이에 도달한 사람들을 리스트에 추가
        call_order[depth].append(curr)

        # 인접 리스트에 연락 가능한 사람이 있는지 확인
        # if curr in matrix:
        for next_p in matrix[curr]:
            if not visited[next_p]:
                visited[next_p] = True
                q.append((next_p, depth + 1))

    # 가장 마지막 깊이에 있는 사람들 중 가장 큰 번호 반환
    # return max(call_order[max_depth])

for tc in range(1, T+1):
    # 입력받는 데이터의 길이, 시작지점
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    visited = [False] * 101
    call_order = [[] for _ in range(101)]

    matrix = [[] for _ in range(101)]
    for i in range(0, N, 2):
        s, e = arr[i], arr[i+1]
        # if s not in matrix:
        #     matrix[s] = []
        matrix[s].append(e)

    # ans = BFS(M)
    # print(f"#{tc} {ans}")

    BFS(M)
    # print(call_order)
    res = []
    for i in range(0, len(call_order) - 1):
        if call_order[i]:
            res.append(call_order[i])


    print(f"#{tc} {max(res[-1])}")


