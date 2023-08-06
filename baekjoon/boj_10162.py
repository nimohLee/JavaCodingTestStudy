T = int(input())
count = [0] * 3

while T > 0:
    if T < 10:
        break
    if T >= 300:
        count[0] += 1
        T = T - 300
    elif T >= 60:
        count[1] += 1
        T = T - 60
    elif T >= 10:
        count[2] += 1
        T = T - 10
if T > 0:
    print(-1)
else:
    print(*count)