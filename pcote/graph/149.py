n, m = map(int, input().split())

graph = []
visited = [[False] * m for _ in range(n)]
cnt = 0

for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if visited[x][y] or graph[x][y] == 1:
        return False

    visited[x][y] = True

    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)

    return True


for i, g in enumerate(graph):
    for j, gi in enumerate(g):
        if dfs(i, j):
            cnt += 1

print(cnt)