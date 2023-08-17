S = str(input())
upper_list = []
answer = []
for i in S:
    if i.isupper():
        upper_list.append(i)

for i in upper_list:
    if len(answer) == 0:
        if i == 'U':
            answer.append(i)    
    else:
        if i == 'C':
            if answer[-1] == 'U' and len(answer) == 1:
                answer.append(i)
            elif answer[-1] == 'P':
                answer.append(i)
                break
        elif i == 'P':
            if answer[-1] == 'C':
                answer.append(i)

if len(answer) == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')