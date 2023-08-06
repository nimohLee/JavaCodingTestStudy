from collections import deque

n, k = map(int, input().split())

MAX = 10 ** 5
dist = [0] * (MAX + 1)
def bfs(s):
    q = deque()
    q.append(s)

    while q:
        cur = q.popleft()
        if cur == k:
            return dist[k]
        for i in (cur+1, cur-1, cur * 2):
            if 0 <= i <= MAX and not dist[i]: 
              dist[i] = dist[cur] + 1
              q.append(i)
print(bfs(n))