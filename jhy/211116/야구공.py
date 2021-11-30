import sys
from itertools import permutations
input = sys.stdin.readline
    
n = int(input())
results = [list(map(int, input().split())) for _ in range(n)]
 
maxScore = -1
 
for order in permutations((range(1, 9)), 8):
    order = list(order[:3]) + [0] + list(order[3:])
    hitter = 0
    score = 0
    for i in range(n):
        out = 0
        first, second, third = 0, 0, 0
 
        while out < 3:           
            result = results[i][order[hitter]]
            
            if result == 0:
                out +=1
            elif result == 1:
                score += third
                first, second, third = 1, first, second
            elif result == 2:
                score += (second + third)
                first, second, third = 0, 1, first
            elif result == 3:
                score += (first + second + third)
                first, second, third = 0, 0, 1
            elif result == 4:
                score += (first + second + third + 1)
                first, second, third = 0, 0, 0
      
            hitter = (hitter + 1) % 9              
    if maxScore < score:
        maxScore = score
 
print(maxScore)