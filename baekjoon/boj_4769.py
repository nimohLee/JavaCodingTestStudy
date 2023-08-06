answer = []
i = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    quotient = ((V // P) * L)
    remainder = V % P
    count = quotient + remainder if remainder <= L else quotient + L
        
    answer.append(f'Case {i}: {count}')
    i += 1

for a in answer:
    print(a)