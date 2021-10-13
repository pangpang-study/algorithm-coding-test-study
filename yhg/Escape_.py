import sys
from collections import deque
input = sys.stdin.readline

n,t,g = map(int, input().split())

count = 0
cal_check_queue = deque()
cal_check_queue.append([0,n])
result = [1e9]
visited = [False] * 100000
visited[n] = True 
def escape(cal_check_queue,chance,target):
    
    while cal_check_queue:
        cnt , cal_check = cal_check_queue.popleft()
        

        if cal_check == target:
            result.append(cnt)
            continue

        if cnt == chance :
            continue

        if cal_check+1 <= 99999: 
            if visited[cal_check+1] == False:
                cal_check_queue.append([cnt +1 , cal_check+1])
                visited[cal_check+1] = True
                
        if cal_check != 0:
            cal_check *= 2
            if cal_check<=99999 :
                string_check = str(cal_check)
                string_check = str(int(string_check[0]) -1) + string_check[1:]
                if visited[int(string_check)] == False:
                    visited[int(string_check)] = True
                    cal_check_queue.append([cnt+1 , int(string_check)])

escape(cal_check_queue, t, g)

answer = min(result)
if answer == 1e9:
    print("ANG")
else:
    print(answer)
