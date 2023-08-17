import sys

T = int(input())

answer = []
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    min_diff = sys.maxsize
    for i in range(1, N):
        if i == N-1 and L[i] - L[0] >= 0:
            min_diff = min(min_diff, (L[i] - L[0]))
        elif L[i] - L[i-1] >= 0:
            min_diff = min(min_diff, (L[i] - L[i-1]))
    answer.append(min_diff)
for i in answer:
    print(i)