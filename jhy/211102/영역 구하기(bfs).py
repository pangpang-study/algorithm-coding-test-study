def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    count = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if(0 <= nx < n) and (0 <= ny < m) and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append((ny, nx))
                count += 1
    
    return count

from collections import deque
import sys

input = sys.stdin.readline

m, n, k = map(int, input().split())

graph = [[0] * n for i in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
            
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

rects = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            rects.append(bfs(i, j))
            
print(len(rects))
print(*sorted(rects))