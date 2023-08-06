from collections import deque

n = int(input())

maze = [[0] * n for _ in range(n)]
for i in range(n):
    maze[i] = [int(digit) for digit in input()]

count_list = []
def bfs(x, y):
    queue = deque()
    visited = set()
    visited.add((x, y))
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    count = 1
    
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= n:
                continue
            if maze[next_x][next_y] == 0:
                continue
            if (next_x, next_y) not in visited:
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                maze[next_x][next_y] = 0
                count += 1
        
    return count

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 1:
            count_list.append(bfs(i, j))

count_list.sort()
print(len(count_list))
for count in count_list:
    print(count)