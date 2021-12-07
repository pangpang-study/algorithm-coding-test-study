import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    
    n = int(input())
    
    result = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        
        start = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** 0.5
        end = ((x2 - cx) ** 2 + (y2 - cy) ** 2) ** 0.5
        
        if start < r and end >= r:
            result += 1
        elif start >= r and end < r:
            result += 1
            
    print(result)