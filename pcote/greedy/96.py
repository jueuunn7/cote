n, m = map(int, input().split())

graph = sorted(list(sorted(map(int, input().split())) for _ in range(n)))
target = sorted([g[0] for g in graph])

print(target[-1])