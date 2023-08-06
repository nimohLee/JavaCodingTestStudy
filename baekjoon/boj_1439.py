from collections import Counter
s = input()

count_zero, count_one = 0, 0
isZero = True if s[0] == '0' else False

for i in s:
    if isZero:
        if i == '1':
          isZero = False
          count_zero += 1
    else:
       if i == '0':
          isZero = True
          count_one += 1
if isZero:
   count_zero += 1
else:
   count_one += 1
print(min(count_zero, count_one))