import sys
from itertools import combinations
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
1~N까지의 번호가 있고 두 개의 선거구로 나눠야한다. 각 구
인구수 차이를 최소로 만들어야한다.

순열로 조합을 만들어서 모든 경우의 수를 탐색하며, 최소값을 넘어서는 순간 바로 다음 반복으로 넘어간다.
선거구로 나눌 수 없으면 -1을 출력한다.
"""

def is_connected(nodes):
    # 그룹 내 구역들이 모두 연결되어 있는지 BFS로 확인
    if not nodes: return False
    q = deque([nodes[0]])
    visited = {nodes[0]}
    count = 1

    while q:
        curr = q.popleft()
        for n in adj_list[curr]:
            # 내 팀이고 아직 방문 안했다면
            if n in nodes and n not in visited:
                visited.add(n)
                q.append(n)
                count += 1
    return count == len(nodes)

# 구역의 개수
N = int(input())
# 각 구역별 인구수
pop = list(map(int, input().split()))
adj_list = [[] for _ in range(N + 1)]

for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    adj_list[i] = tmp[1:]

all_nodes = list(range(1, N + 1))
min_diff = float('inf')

# 모든 조합 탐색
for i in range(1, N // 2 + 1):
    for combo in combinations(all_nodes, i):
        group_a = list(combo)
        group_b = [node for node in all_nodes if node not in group_a]

        # 두 그룹 모두 연결되어 있는지 확인
        if is_connected(group_a) and is_connected(group_b):
            pop_a = sum(pop[node-1] for node in group_a)
            pop_b = sum(pop[node-1] for node in group_b)
            min_diff = min(min_diff, abs(pop_a - pop_b))

if min_diff == float('inf'):
    print(-1)
else:
    print(min_diff)