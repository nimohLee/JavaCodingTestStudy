n = int(input())
count = 0
while True:
    if n % 5 == 0:
        count += n // 5
        break
    if n == 1:
        count = -1
        break
    n -= 2
    count += 1
print(count)