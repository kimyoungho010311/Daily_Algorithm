import sys
sys.stdin = open('input.txt')
"""
V개의 해야할 작업이 있다. 이 작업간에는 선행 관계가 있다.
이러한 관계가 그래프로 주어진다. 그래프에 순환은 없다.

가능한 경우의 수를 하나 출력해라.
"""
from collections import deque

def sort():
    result = []
    q = deque()

    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    while q:
        curr = q.popleft()
        result.append(curr)

        for next in graph[curr]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    return result

T = 10
for tc in range(1, T+1):

    # 정점의 수, 간선의 수
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))

    indegree = [0] * (V + 1)
    graph = [[] for _ in range(V + 1)] # 4 1 1 2 2 3 2 7 5 6 7 6 1 5 8 5 8 9


    for i in range(0, len(edges), 2):
        u = edges[i]
        v = edges[i+1]

        graph[u].append(v)
        indegree[v] += 1

    ans = sort()

    print(f"#{tc}", *ans)