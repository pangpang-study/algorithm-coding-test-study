import sys

input = sys.stdin.readline

n = int(input())

regions = list(map(int, input().split()))

budget = int(input())

if sum(regions) <= budget:
    print(max(regions))
    exit()

start, end = 0, max(regions)

while start <= end:
    result = (start + end) // 2
    
    total = 0

    for i in regions:
        total += min(result, i)
        
    if total > budget:
        end = result - 1
    else:
        start = result + 1

print(end)