import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

kids = list(map(int,input().split()))
cost = []
for i in range(n-1):
    cost.append(kids[i+1] - kids[i])

cost = sorted(cost)

result = 0 
for i in range(n-k):
    result += cost[i]

print(result)