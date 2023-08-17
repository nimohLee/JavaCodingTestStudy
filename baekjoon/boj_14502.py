from collections import deque

N = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]
answer = []
def bfs(x, y, cur_graph):
    q = deque();
    q.append((x, y, 0))
    while q:
        cur_x, cur_y, count = q.popleft()
        if cur_x == end_x and cur_y == end_y:
            return count
        for i in range(8):
            next_x, next_y =  cur_x + dx[i], cur_y + dy[i]
            if next_x < 0 or next_y < 0 or next_x >= I or next_y >= I:
                continue
            if cur_graph[next_x][next_y] == 0:
                q.append((next_x, next_y, count + 1))
                cur_graph[next_x][next_y] = 1
    return 0

for i in range(N):
    I = int(input())
    graph = [[0] * I for _ in range(I)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    answer.append(bfs(start_x, start_y, graph))

for i in answer:
  print(i)