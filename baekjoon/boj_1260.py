from collections import deque

n, m, v = map(int, input().split())

graph = dict()

for i in range(1, n+1):
  graph[i] = list()

for i in range(1, m+1):
    start_v, end_v = map(int, input().split())
    graph[start_v].append(end_v)
    if start_v not in graph[end_v]:
        graph[end_v].append(start_v)    

for i in graph:
   graph[i].sort()

dfs_visited = list()
bfs_visited = list()
    
def dfs(start_v):
    dfs_visited.append(start_v)
    for next_v in graph[start_v]:
       if next_v not in dfs_visited:
          dfs(next_v)
    
def bfs(start_v):
    q = deque()
    bfs_visited.append(start_v)
    q.append(start_v)
    while q:
        cur_v = q.popleft()
        for next_v in graph[cur_v]:
          if next_v not in bfs_visited:
            q.append(next_v)
            bfs_visited.append(next_v)
dfs(v)
bfs(v)

print(*dfs_visited)
print(*bfs_visited)