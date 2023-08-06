from collections import deque

n = int(input())
m = int(input())

graph = dict()

for i in range(1, n+1):
  graph[i] = list()

for i in range(1, m+1):
    start_v, end_v = map(int, input().split())
    graph[start_v].append(end_v)
    if start_v not in graph[end_v]:
        graph[end_v].append(start_v)    
    
def bfs(start_v):
    q = deque()
    q.append(start_v)
    visited = []
    while q:
        cur_v = q.popleft()
        for next_v in graph[cur_v]:
          if next_v not in visited:
            q.append(next_v)
            visited.append(next_v)
    return len(visited) - 1

bfs(1)
print(bfs(1))