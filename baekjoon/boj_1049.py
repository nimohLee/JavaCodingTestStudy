N, M = map(int, input().split())
packages, singles = [], []
for _ in range(M):
    pack, single = map(int, input().split())
    packages.append(pack)
    singles.append(single)

min_pack_price, min_single_price = min(packages), min(singles)
if (min_pack_price // 6) >= min_single_price:
    price = min_single_price * N
else:
    price = ((N // 6 * min_pack_price)) + ((N % 6) * min_single_price)
if price >= ((N // 6 + 1) * min_pack_price):
    price = ((N // 6 + 1) * min_pack_price)
print(price)