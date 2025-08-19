graph = [[] for _ in range(int(input()) + 1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start = 1
visited = [False] * (len(graph))
stack = [start]
result = []

while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        result.append(node)
        for nei in graph[node]:
            if not visited[nei]:
                stack.append(nei)

result.remove(start)
print(len(result))