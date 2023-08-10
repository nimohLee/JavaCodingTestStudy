N = int(input())
houses = list(map(int, input().split()))
houses.sort()
answer = 0
if N % 2 == 0:
    answer = houses[(N // 2) - 1]
else:
    answer = houses[N // 2]
print(answer)