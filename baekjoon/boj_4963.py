from collections import deque

answer = []
vect = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited.add((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(8):
          next_x, next_y = cur_x + vect[i][0], cur_y + vect[i][1]
          if next_x < 0 or next_y < 0 or next_x >= h or next_y >= w:
              continue
          if (next_x, next_y) not in visited and graph[next_x][next_y] == 1:
              q.append((next_x, next_y))
              visited.add((next_x, next_y))
    return 1

while True:
    w, h = map(int, input().split())
    visited = set()
    count = 0
    if w == 0 and h == 0:
        break
    graph = [[[0] * w] for _ in range(h)]
    for i in range(h):
        graph[i] = list(map(int, input().split()))
    for i in range(h):
        for j in range(w):
            if (i, j) not in visited and graph[i][j] == 1:
              count += bfs(i, j)
    answer.append(count)

for i in answer:
    print(i)