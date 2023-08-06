import heapq
n = int(input())

cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)
cnt = 0
while len(cards) > 1:
    sum = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, sum)
    cnt += sum

print(cnt)
