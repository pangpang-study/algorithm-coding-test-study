import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
c = int(input())
d = []

for _ in range(n):
    d.append(int(input()))

d.sort(reverse=True)

kcal = c
cost = a
result = c // a

for i in d:
    kcal += i
    cost += b
    
    kcal_per_won = kcal // cost
    if result > kcal_per_won:
        break
    else:
        result = kcal_per_won
        
print(result)