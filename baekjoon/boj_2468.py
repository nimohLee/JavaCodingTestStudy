from collections import deque

def rain_bfs(x, y, h):
    q = deque()
    q.append((x, y))
    visited.add((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= n:
                continue
            if (next_x, next_y) not in visited and graph[next_x][next_y] > h:
                q.append((next_x, next_y))
                visited.add((next_x, next_y))

n = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = [[0] * n for _ in range(n)]
answer = 0
max_num = 0
for i in range(n):
    graph[i] = list(map(int, input().split()))
    max_num = max(max_num, max(graph[i]))

max_count = 0
for i in range(0, max_num + 1):
    cur_count = 0
    visited = set()
    for x in range(n):
        for y in range(n):
            if graph[x][y] > i and (x, y) not in visited:
                rain_bfs(x, y, i)
                cur_count += 1
    max_count = max(max_count, cur_count)

print(max_count)
