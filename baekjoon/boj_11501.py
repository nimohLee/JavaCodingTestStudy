T = int(input())
answer = []
for i in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))
    stocks.reverse()
    max_price = 0
    gain = 0
    for stock in stocks:
        if stock < max_price:
            gain += (max_price - stock)
        else:
            max_price = stock
    answer.append(gain)

for i in answer:
    print(i)