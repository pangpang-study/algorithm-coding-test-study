import sys

input = sys.stdin.readline

n = int(input())

in_list, out_list = {}, []

order = 0
for _ in range(n):
    in_list[input().rstrip()] = order
    order += 1
    
for _ in range(n):
    out_list.append(str(input().rstrip()))

count = 0

while len(out_list) >= 2:
    next = out_list[-1]
    pre = out_list[-2]
    
    if in_list[pre] > in_list[next]:
        out_list.remove(pre)
        count += 1
    else:
        out_list.remove(next)
        
print(count)