from queue import PriorityQueue

n, m = map(int, input().split())
que = PriorityQueue()
cards = list(map(int, input().split()))
for card in cards:
    que.put(card)

for _ in range(m):
    x, y =  que.get(), que.get()
    que.put(x+y)
    que.put(x+y)
sum = 0
for _ in range(que.qsize()):
    sum += que.get()
print(sum)


