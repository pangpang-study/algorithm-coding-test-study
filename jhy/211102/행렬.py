def op(x, y):
    for i in range(3):
        for j in range(3):
            if A[y + i][x + j] == 1:
                A[y + i][x + j] = 0
            else:
                A[y + i][x + j] = 1

n, m = map(int, input().split())

A = [list(map(int, input().rstrip())) for _ in range(n)]

B = [list(map(int, input().rstrip())) for _ in range(n)]

if A == B:
    print(0)
    exit()
    
if (n or m) < 3:
    print(-1)
    exit()

count = 0

for a in range(n - 2):
    for b in range(m - 2):
        if A[a][b] != B[a][b]:
            op(b, a)
            count += 1
     
if A == B:
    print(count)
else:
    print(-1)