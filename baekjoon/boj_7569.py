from collections import deque

m, n, h = map(int, input().split())

box = [[[0] * m for _ in range(n)] for _ in range(h)]

isAllOne = True
result = 0
for i in range(h):
    for j in range(n):
        box[i][j] = list(map(int, input().split()))
        if box[i][j].count(1) != m:
           isAllOne = False

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

visited = set()

q = deque()

def bfs():
   while q:
      cur_h, cur_n, cur_m = q.popleft()
      for i in range(6):
         next_h, next_n, next_m = cur_h + dz[i], cur_n + dy[i], cur_m + dx[i]
         if next_h < 0 or next_n < 0 or next_m < 0:
            continue
         if next_h >= h or next_n >= n or next_m >= m:
            continue
         if box[next_h][next_n][next_m] == 0 and (next_h, next_n, next_m) not in visited:
            box[next_h][next_n][next_m] = box[cur_h][cur_n][cur_m] + 1
            q.append((next_h, next_n, next_m))
            visited.add((next_h, next_n, next_m))

if not isAllOne:
   for i in range(h):
    for j in range(n):
        for z in range(m):
          if box[i][j][z] == 1 and (i,j,z) not in visited:
              q.append((i, j, z))
              visited.add((i, j, z))

bfs()

for a in box:
   for b in a:
      for c in b:
         if c == 0:
            print(-1)
            exit(0)
      result = max(result, max(b))

print(result)