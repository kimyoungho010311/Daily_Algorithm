from collections import deque
def bfs(start):
    nodes = list(graph.keys())
    visited = [False] * len(nodes)
    q = deque([start])
    result = []

    start_index = nodes.index(start)
    visited[start_index] = True

    while q:
        vertex = q.popleft()
        result.append(vertex)

        for neighbor in graph[vertex]:
            neighbor_index = nodes.index(neighbor)
            if not visited[neighbor_index]:
                q.append(neighbor)
                visited[neighbor_index] = True
    return result


graph = {
    'A': ['B', 'C'],
    'B': ["A","D","E"]
    ,"C": ["A"]
    ,"D": ["B","F"]
    ,"E": ["B","F"]
    ,"F": ["D","E", "G"]
    ,"G": ["F"]
}

nodes = list(graph.keys())
visited = [False] * len(nodes)
result = []

for node in nodes:
    if not visited[nodes.index(node)]:
        result.extend(bfs(node))
print("그래프 탐색 경로: ", result)