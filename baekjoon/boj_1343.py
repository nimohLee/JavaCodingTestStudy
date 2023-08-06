s = input().split('.')
A = 'AAAA'
B = 'BB'

for i in range(len(s)):
    x_len = len(s[i])
    if x_len % 2 != 0:
        print(-1)
        exit(0)
    elif s[i] == '':
        continue
    else:
        s[i] = A * (x_len // 4)
        s[i] += B if x_len % 4 != 0 else ''

print('.'.join(s))