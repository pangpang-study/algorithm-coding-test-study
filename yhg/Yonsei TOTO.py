import sys
from collections import deque
input = sys.stdin.readline

n , m = map(int, input().split())

m_candi = []
for i in range(n):
    now_candi , max_candi = map(int, input().split())
    now_m = deque(map(int, input().split()))
    now_m = deque(sorted(now_m))

    if now_candi < max_candi:
        m_candi.append(1)
        continue
    
    while len(now_m)> max_candi :
        now_m.popleft()

    m_candi.append(now_m.popleft())

m_candi = sorted(m_candi)

result = 0 
count = 0 
for m_c in m_candi:
    if count + m_c <= m:
        count += m_c
        result +=1
    else:
        break
print(result)
