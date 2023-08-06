from itertools import combinations

n, k = map(int, input().split())

weight = []
combi = []
max_value = 0
for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    items[w] = v

for i in range(1, n + 1):
    combi.extend(combinations(weight, i))
weight = []

for i in combi:
    cur_w = 0
    value = 0
    for j in i:
        cur_w += j
        value += items[j]
    if cur_w <= k:
        max_value = max(max_value, value) 

print(max_value)
