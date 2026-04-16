import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
"""
N명의 학생을을 키 순서로 정렬할려고 한다.
일부 학생들만 키 조사를 하였다.

왜 위상정렬인가?
1. 우선순위 존재: A -> B 순서로 줄을 세워야 한다.
2. 사이클 없음: A -> B -> A 와 같은 경우는 없다.
3. 위 조건들을 지키면서 정렬해야한다.

해결전략 (Kahn Algorithm)
1. 진입차수(ingree) 배열을 만든다.
2. 인접 리스트를 만든다.
3. 진입차수가 0인 학생들을 큐에 넣는다.
4. 큐가 빌 때까지 반복을한다.

"""
from collections import deque

def sort():
    result = []
    q = deque()

    # 진입차수가 0인 학생들을 큐에 먼저 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        curr = q.popleft()
        result.append(curr)

        # 현재 학생 뒤에 서야 하는 학생들 확인
        for next_student in graph[curr]:
            indegree[next_student] -= 1
            # 앞에 서야 할 사람이 더 이상 없으면 큐에 샆입
            if indegree[next_student] == 0:
                q.append(next_student)

    print(*result)
# 학생 수, 비교 횟수
N, M = map(int, input().split())

# 진입차수, 인접 리스트
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

sort()