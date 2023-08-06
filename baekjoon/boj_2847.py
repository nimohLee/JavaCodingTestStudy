n = int(input())
dist = [int(input()) for _ in range(n)]
dist = dist[::-1]
count = 0

for i in range(1, len(dist)):
    if dist[i] >= dist[i-1]:
        count += dist[i] - (dist[i-1] - 1)
        dist[i] = dist[i-1] - 1

print(count)
