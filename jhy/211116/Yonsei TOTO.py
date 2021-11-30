def get_sub(m, p, l, points):
    if p < l:
        if m >= 1:
            result.append(1)
    elif p == l:
        if m >= min(points):
            result.append(min(points))
    else:
        points.sort()
        for i in range(l - 1):
            points.pop()
        point = points.pop()

        if m >= point:
            result.append(point)
    return

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
result = []

for _ in range(n):
    p, l = map(int, input().split())
    points = list(map(int, input().split()))
    get_sub(m, p, l, points)
  
result.sort()
count = 0

for i in range(len(result)):
    if m >= result[i]:
        m -= result[i]
        count += 1
    else:
        break
            
print(count)