import sys
sys.stdin = open('input.txt')
"""
N개의 집, M개의 길로 이루어져 있다.
각 길을 유지하는데 비용이 든다.
임의의 두 집 사이에 경로가 항상 존재한다.

두 마을로 분리해야 한다.
분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다.
마을에는 하나 이상의 집이 있어야 한다.

길 없애기
두 마을의 길을 없앤다.
마을 안에서 임의의 두 집 사이의 길을 없앤다.(최소 한개는 남겨야 한다.)

유지비의 최소 합을 출력해라
=============================
두 마을 분리하기 로직은 생각보다 간단하다.
애초에 MST로직이 하나의 트리(마을)을 최소 비용으로 만드는 로직이다.
이렇게 만들어진 MST에서 간선 하나만 제거해도 두 개의 트리(마을)을 만들어진다.

특히 크루스칼은 가중치의 정렬에 따라 MST를 만들기 떄문에 가장 마지막 간선(길)만 지우면
간단하게 두 개의 마을이 생기기 떄문에 너무 복잡한 문제는 아니다.
"""
import sys
input = sys.stdin.readline
def make_set(x):
    parent = list(range(x+1))
    rank = [0] * (x+1)
    return parent, rank

def find_set(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

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

def same(x, y):
    return find_set(x) == find_set(y)

# 집의 개수, 길의 개수
N, M = map(int, input().split())

parent, rank = make_set(N)
roots = []
min_cost = 0
max_edge = 0
cnt_node = 0

for _ in range(M):
    s, e, w = map(int, input().split())
    roots.append((s, e, w))

roots.sort(key=lambda x: x[2])
# print(roots)
for s, e, w in roots:
    if not same(s, e):
        union(s, e)
        min_cost += w
        max_edge = w
        cnt_node += 1
    if cnt_node == N - 1:
        break
print(min_cost - max_edge)