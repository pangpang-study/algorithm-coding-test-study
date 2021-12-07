import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

n= int(input())

visited = set()
result = 0
def cal_score(order , member):
    score = 0 
    global result
    hit_num = 0
    for i in range(n):
        out_count = 3
        base = deque([0,0,0])
        while out_count > 0:
            hit_num += 1
            if hit_num % 9 == 4:
                now = 1
            else:
                now = order.popleft()

            if member[i][now] == 1:
                base.appendleft(1)
            elif member[i][now] == 2:
                base.appendleft(1)
                base.appendleft(0)
            elif member[i][now] == 3:
                base.appendleft(1)
                base.appendleft(0)
                base.appendleft(0)
            elif member[i][now] == 4:
                score += sum(base)+1
                base = deque([0,0,0])
            elif member[i][now] == 0:
                out_count -= 1

            while len(base) > 3:
                if base.pop() == 1:
                    score +=1
                    
            if now != 1:
                order.append(now)
          
    result = max(result , score)
member = [{} for _ in range(n)]
inning = 0
for i in range(n):
    score = deque(map(int, input().split()))
    idx = 1
    for s in score:
        member[inning][idx] = s
        idx +=1
    inning +=1
    

m_order = [2,3,4,5,6,7,8,9]
m_order_per = list(permutations(m_order , len(m_order)))

for m_p in m_order_per:
    if m_p not in visited:
        visited.add(m_p)
        cal_score(deque(m_p) , member)
print(result)

    

