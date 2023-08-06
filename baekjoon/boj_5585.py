price = 1000 - int(input())
count = 0
cashes = [500, 100, 50, 10, 5]
for cash in cashes:
    n = price // cash
    if n > 0:
        price -= (cash * n)
        count += n

# 1원을 제외한 모든 화폐를 뺀 값(price)이 결국 내야하는 1원의 갯수
print(count + price)