from collections import deque
import sys
import os

# input.txt를 스크립트 파일 기준으로 열기
base = os.path.dirname(__file__)
sys.stdin = open(os.path.join(base, 'input.txt'))

N = int(sys.stdin.readline())

adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

parent = [0] * (N + 1)

q = deque([1])
parent[1] = -1

while q:
    cur = q.popleft()
    for nxt in adj[cur]:
        if parent[nxt] == 0:
            parent[nxt] = cur
            q.append(nxt)

for i in range(2, N + 1):
    print(parent[i])