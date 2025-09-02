n, m, k, start = map(int, input().split())

graph = []
info = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs():
    stack = [start]
    visited = [False] * (n + 1)

    while stack:
        node = stack.pop(-1)

        if not visited[node]:
            visited[node] = True

            for nei in graph[node]:
                if not visited[nei]:
                    stack.append(nei)

dfs()