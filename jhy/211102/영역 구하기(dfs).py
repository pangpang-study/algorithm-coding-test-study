def dfs(y, x, count):
    graph[y][x] = 1
    
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        
        if (0 <= ny < m) and (0 <= nx < n) and graph[ny][nx] == 0:
            count = dfs(ny, nx, count + 1)
            
    return count

import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    
    for j in range(y1, y2):
        for k in range(x1, x2):
            graph[j][k] = 1

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

rects = []
        
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            rects.append(dfs(i, j, 1))

print(len(rects))
print(*sorted(rects))