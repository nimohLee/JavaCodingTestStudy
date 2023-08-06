# question = input()
# digits = []
# operations = []
# tmp_num = ''
# answer = 0
# for i in question:
#     if i.isdigit():
#         tmp_num += i
#     else:
#         digits.append(int(tmp_num))
#         tmp_num = ''
#         operations.append(i)
# digits.append(int(tmp_num))
# if len(digits) == 0:
#     print(0)
#     exit(0)

# tmp_num = 0
# isMinus = False
# for i in range(len(digits)):
#     if i == 0:
#         answer+= digits[i]
#         continue
#     if isMinus:
#         if operations[i-1] == '+':
#             tmp_num += digits[i]
#         else:
#             answer -= tmp_num
#             answer -= digits[i]
#             isMinus = False
#     else:
#         if operations[i-1] == '+':
#             answer += digits[i]
#         else:
#             isMinus = True
#             tmp_num += digits[i]
# if tmp_num:
#     answer -= tmp_num
# print(answer)         



arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)