n = int(input())

ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=True)
answer = []
for i in range(len(ropes)):
    answer.append(ropes[i] * (i+1))

print(max(answer))