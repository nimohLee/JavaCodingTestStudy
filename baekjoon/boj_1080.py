def reverseMatrix(matrix, x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            matrix[i][j] = 1 - matrix[i][j]

def check():
  for i in range(N):
    for j in range(M):
      if A[i][j] != B[i][j]:
        return False
  
  return True

N, M = map(int, input().split())

A, B = [], []
for _ in range(N):
  A.append(list(map(int, input())))

for _ in range(N):
  B.append(list(map(int, input())))

if N < 3 or M < 3:
  print(-1)
  exit(0)
count = 0
for i in range(N-2):
  for j in range(M-2):
    if A[i][j] != B[i][j]:
      reverseMatrix(A, i, j)
      count += 1

# reversed = set()
# while True:
#   a, b = findDiff(A, B)
#   reverseMatrix(A, a, b)
#   if (a, b) not in reversed:
#     reversed.add((a, b))
#   else:
#     count = -1
#     break  
#   count += 1
#   if A == B:
#     break
if check():
  print(count)
else:
  print(-1)
