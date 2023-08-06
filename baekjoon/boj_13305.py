n = int(input())
distance = list(map(int, input().split()))
town = list(map(int, input().split()))
min_price = town[0]
price = 0
for i in range(len(distance)):
    if min_price > town[i]:
        min_price = town[i]
    price += min_price * distance[i]
    
print(price)