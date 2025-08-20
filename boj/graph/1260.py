n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, n + 1):
    graph[i].sort()


def dfs(start):
    visited = [False] * (n + 1)
    stack = [start]

    while stack:
        node = stack.pop(-1)
        if not visited[node]:
            visited[node] = True
            print(node, end=" ")
            for nei in sorted(graph[node], reverse=True):
                if not visited[nei]:
                    stack.append(nei)


def bfs(start):
    visited = [False] * (n + 1)
    queue = [start]
    visited[start] = True

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for nei in graph[node]:
            if not visited[nei]:
                queue.append(nei)
                visited[nei] = True


dfs(v)
print("")
bfs(v)