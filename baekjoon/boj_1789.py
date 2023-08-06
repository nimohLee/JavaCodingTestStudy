s = int(input())
count = 0
sum = 0
for i in range(1, s+1):
    if s - (sum + i) <= i:
        break
    count += 1
    sum += i
print(count+1)