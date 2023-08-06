from collections import deque

n, m = map(int, input().split())

maze = [[0] * m for _ in range(n)]
answer = 0
for i in range(n):
    maze[i] = [int(digit) for digit in input()]

visited = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y, 1))
    visited.add((x, y))
    count = 1
    while q:
        cur_x, cur_y, cur_count = q.popleft()
        if cur_x == n - 1 and cur_y == m - 1:
            count = cur_count
            break
        for i in range(4):
          next_x = cur_x + dx[i]
          next_y = cur_y + dy[i]
          if next_x < 0 or next_y < 0:
              continue
          if next_x >= n or next_y >= m:
              continue
          if maze[next_x][next_y] == 0:
              continue
          if (next_x, next_y) not in visited:
              visited.add((next_x, next_y))
              q.append((next_x, next_y, cur_count + 1))    
          
    return count

print(bfs(0, 0))
        