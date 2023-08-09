N = int(input())
S = str(input())

ll_count = S.count("LL")
if ll_count > 0:
    print(N - (ll_count - 1))
else:
    print(N)