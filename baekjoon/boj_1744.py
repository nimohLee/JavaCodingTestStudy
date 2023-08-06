N = int(input())
plus = []
minus = []
for _ in range(N):
    num = int(input())
    if num > 0:
        plus.append(num)
    else:
        minus.append(num)
plus.sort(reverse=True)
minus.sort()

stack = []
answer = 0
for i in plus:
    if i == 0 or i == 1:
        answer += i
    elif not stack:
        stack.append(i)
    else:
        answer += stack.pop() * i
if stack:
    answer += stack.pop()

for i in minus:
    if i == 0:
        if stack:
            answer += stack.pop() * 0
        break
    if not stack:
        stack.append(i)
    else:
        answer += stack.pop() * i
if stack:
    answer += stack.pop()

print(answer)