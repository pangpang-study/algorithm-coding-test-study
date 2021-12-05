import sys
from collections import deque

n , m , r  = map(int, input().split())

item_list = list(map(int, input().split()))
locations = [[] for _ in range(n+1)]

graph = [[1e9] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0
            
for i in range(r):
    left , right , cost = map(int, input().split())
    graph[left][right] = cost
    graph[right][left] = cost

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0

for i in range(1, n+1):
    count = 0 

    for j in range(1, n+1):
        if graph[i][j] <= m:
            count += item_list[j-1]
    
    result = max(result , count)

print(result)

    
