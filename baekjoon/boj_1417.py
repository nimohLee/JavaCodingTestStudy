N = int(input())
dasom = int(input())
candidate = []

for i in range(N-1):
    vote = int(input())
    candidate.append(vote)

if N == 1:
    print(0)
    exit(0)

candidate.sort(reverse=True)
count = 0
while candidate[0] >= dasom:
    candidate[0] -= 1
    dasom += 1
    count += 1
    candidate.sort(reverse=True)

print(count)