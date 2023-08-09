from collections import deque
import sys

N = int(input())
graph = {}
parents = {}
for i in range(1, N+1):
    graph[i] = []

for i in range(N-1):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def bfs(start_v):
    q = deque()
    visited = set()
    q.append(start_v)
    visited.add(start_v)
    while q:
        cur_v = q.popleft()
        for i in graph[cur_v]:
            if i not in visited:
                parents[i] = cur_v
                q.append(i)
                visited.add(i)

bfs(1)
for i in range(2, len(parents)+2):
    print(parents[i])