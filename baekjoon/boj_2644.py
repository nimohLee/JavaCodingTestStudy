from collections import deque

n = int(input())
start_v, end_v = map(int,input().split())

graph = {}

for i in range(1, n + 1):
    graph[i] = []

for _ in range(int(input())):
    from_v, to_v = map(int, input().split())
    graph[from_v].append(to_v)
    if from_v not in graph[to_v]:
        graph[to_v].append(from_v)

def bfs(start_v, end_v):
    visited = [start_v]
    chon = -1
    q = deque()
    q.append((start_v, 0))
    while q:
        cur_v, cur_chon = q.popleft()
        if cur_v == end_v:
            chon = cur_chon
            break
        for v in graph[cur_v]:
            if v not in visited:
                q.append((v, cur_chon + 1))
                visited.append(v)
    return chon

visited = []
find_chon = -1
def dfs(v, chon):
    global find_chon
    if v == end_v:
        find_chon = chon
        return

    for v in graph:
        if v not in visited:
            visited.append(v)
            dfs(v, chon + 1)

# print(bfs(start_v, end_v))
dfs(start_v, 0)
print(find_chon)