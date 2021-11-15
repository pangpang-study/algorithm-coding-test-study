import sys
from collections import deque
input = sys.stdin.readline


n = int(input())

info = list(map(int, input().split()))

line_queue = deque()

for i in range(n, 0 , -1):
    right_queue = deque()
    
    if info[i-1] == n-i:
        line_queue.append(i)
    else:
        while True:
            right_queue.appendleft(line_queue.pop())
            info[i-1]+=1
            if info[i-1] == n-i:
                line_queue.append(i)   
                break
    
    while right_queue:
        line_queue.append(right_queue.popleft())

for i in list(line_queue):
    print(i , end = " ")