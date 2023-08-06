import sys
n = int(sys.stdin.readline())
answer = []
score = [[0] for _ in range(n)]

for i in range(n):
  dist = []
  t = int(sys.stdin.readline())
  for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    dist.append((a, b))
  score[i] = dist

for a in score:
  count = 0
  a.sort()
  base = a[0][1]
  for i in range(len(a)):
    if a[i][1] <= base:
      base = a[i][1]
      count += 1
  answer.append(count)


for i in answer:
  print(i)
        
