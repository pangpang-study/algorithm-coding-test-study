import sys

input = sys.stdin.readline

s, e, q = map(str, input().split())

before = set()
after = set()

while True:
    try:
        time, id = map(str, input().split())
        if time <= s:
            before.add(id)
            
        elif e <= time <= q:
            after.add(id)
            
        else:
            continue
    except:
        break
    
count = 0

for i in before:
    if i in after:
        count += 1
print(count)