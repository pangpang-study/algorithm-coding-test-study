import sys

input = sys.stdin.readline

n, k = map(int, input().split())
kindergartens = list(map(int, input().split()))

costs = []

for i in range(n-1):
    costs.append(kindergartens[i+1] - kindergartens[i])

costs.sort()

print(sum(costs[:n-k]))