S = list(map(str, input()))
T = list(map(str, input()))

while len(S) < len(T):
    if T.pop() == 'B':
        T = T[::-1]

print(1 if S == T else 0)