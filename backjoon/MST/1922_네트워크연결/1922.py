import sys
sys.stdin = open('input.txt')
"""

"""
# 여기 아래에 코드 ㄱㄱ

def make_set(x):
    parent = list(range(x+1))
    rank = [0] * (x + 1)

    return parent, rank

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])

    return parent[x]

def same(x, y):
    return find_set(x) == find_set(y)

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

# 컴퓨터의 수
N = int(input())
# 간선의 수
M = int(input())
min_cost = 0
cnt_node = 0
parent, rank = make_set(N)
roots = []

for _ in range(M):
    s, e, w = map(int, input().split())
    roots.append((s, e, w))

roots.sort(key=lambda x: x[2])

for s, e, w in roots:

    if not same(s, e): # 같은 부모(그룹)가 아니라면
        union(s, e)
        min_cost += w
        cnt_node += 1
    if cnt_node == N + 1:
        break

print(min_cost)