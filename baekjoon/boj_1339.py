from collections import deque

n = int(input())
words = [input().rstrip() for _ in range(n)]
alpha = {}
i = 0
answer = 0
for word in words:
    cnt = len(word) - 1
    for w in word:
      if w not in alpha:
          alpha[w] = 10 ** cnt
          i += 1
      else:
          alpha[w] += 10 ** cnt
      cnt -= 1

values = sorted(alpha.values(), reverse=True)
cnt = 9
for i in values:
    answer += i * cnt
    cnt -= 1
    

print(answer)