from collections import deque

s = input()
dist = []
queue = deque()

for i in s:
    dist.append(i)
dist.sort()
for i in dist:
    queue.append(i)

palindrome = [''] * len(s)
front, back = 0, -1
while queue:
    if len(queue) == 1:
        palindrome[front] = queue.popleft()
        break
    a,b = queue.popleft(), queue.popleft()
    if a != b:
        print("I'm Sorry Hansoo")
        exit(0)
    palindrome[front], palindrome[back] = a, b
    front += 1
    back -= 1
print(''.join(palindrome))
        