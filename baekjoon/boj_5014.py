from collections import deque

f, s, g, u, d = map(int, input().split())

count = [0 for _ in range(f+1)]
visited = set()
def bfs(start):
    q = deque()
    q.append(start)
    visited.add(start)
    while q:
      cur = q.popleft()
      if cur == g:
         return count[g]
      for i in (cur+u, cur-d):
         if 0 < i <= f and i not in visited:
            visited.add(i)
            count[i] = count[cur] + 1
            q.append(i)
    
    return 'use the stairs'

print(bfs(s))