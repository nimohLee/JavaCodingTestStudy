n = input()

sorted_n = sorted(n, reverse=True)
sum = 0
if int(sorted_n[-1]) != 0:
    print(-1)
else:
    for i in sorted_n:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        print(''.join(sorted_n))