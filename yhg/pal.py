import sys
from collections import deque
input = sys.stdin.readline

l , r = map(int, input().split())

l_queue = deque(str(l))
r_queue = deque(str(r))

result = 0 
if len(l_queue) != len(r_queue):
    print(0)
else:
    if l_queue[0] != r_queue[0]:
        print(0)
    else:
        l_n = l_queue.popleft()
        r_n = r_queue.popleft()
        
        if l_n == '8':
            result += 1

        while l_queue:
            l_n = l_queue.popleft()
            r_n = r_queue.popleft()
            if l_n != r_n :
                break
            elif l_n == '8' and r_n == '8': 
                result +=1
    
        print(result)
