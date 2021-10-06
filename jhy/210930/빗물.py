import sys

h, w = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

height = min(array[0], max(array[1:]))

result = 0

for i in range(w - 1):
    gap = height - array[i]

    if gap > 0:
        
        result += gap
    else:
        height = min(array[i], max(array[i + 1:]))

print(result)