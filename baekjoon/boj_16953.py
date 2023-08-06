A, B = map(int, input().split())

count = 0
while True:
    if B == A:
        break
    elif A > B:
        count = -2
        break
    elif str(B)[-1] == '1':
        B = int(str(B)[:-1])
        count += 1
        continue
    elif B % 2 == 0:
        B //= 2
        count += 1
        continue
    else:
        count = -2
        break

print(count+1)    