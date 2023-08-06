import sys
from collections import deque

visited = set()

def bfs(start_v):
    q = deque()
    q.append(start_v)
    visited.add(start_v)
    while q:
        cur_v = q.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                q.append(v)
                visited.add(v)
    return 1

N, M = map(int, sys.stdin.readline().split())
graph = {}
for i in range(1, N+1):
    graph[i] = []
for i in range(M):
    u, v = map( int, sys.stdin.readline().split() )
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, N+1):
    if i not in visited:
      count += bfs(i)
print(count)