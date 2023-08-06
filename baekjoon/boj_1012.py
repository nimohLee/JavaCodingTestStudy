from collections import deque

answer = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = set()

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited.add((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        graph[cur_x][cur_y] = 0
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if graph[nx][ny] == 1 and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))
    return 1

n = int(input())
for _ in range(n):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    count = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count += 1
                bfs(i, j)
    print(count)