money = []
for i in range(int(input())):
    money.append(int(input()))
for a in money:
    quarter, dime, nickel = 0, 0, 0
    if a >= 25:
        quarter = a // 25
        a %= 25
    if a >= 10:
        dime = a // 10
        a %= 10
    if a >= 5:
        nickel = a // 5
        a %= 5
    print(quarter, dime, nickel, a)
