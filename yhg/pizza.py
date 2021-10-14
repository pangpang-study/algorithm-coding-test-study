import sys
from collections import deque
from bisect import bisect_left , bisect_right
input = sys.stdin.readline

deep , n = map(int , input().split())

oven = list(map(int, input().split()))

pizza = deque(list(map(int , input().split())))

pizza_index = 0

for i in range(1, deep):
    oven[i] = min(oven[i-1] , oven[i])

oven = deque(oven[::-1])

idx = 0 

while pizza:
    p = pizza.popleft()
    
    while oven:
        o = oven.popleft()
        if o < p :
            continue
        else: 
            break

if len(oven) == 0   :
    print(0)
else:
    print(len(oven) +1 )
        




