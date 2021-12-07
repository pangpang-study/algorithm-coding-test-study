import sys

def recur(idx, s):
    global result

    if idx == n:
        count = 0
        for i in range(n):
            if s[i] <= 0:
                count += 1
        
        if count > result:
            result = count
        return
    
    if s[idx] > 0:
        for i in range(n):
            flag = False
            if s[i] > 0 and i != idx:
                flag = True
                tmp = s[:]
                tmp[i] -= w[idx]
                tmp[idx] -= w[i]
                recur(idx + 1, tmp)
        if not flag:
            recur(idx + 1, s)
    else:
        recur(idx + 1, s)
                
input = sys.stdin.readline

n = int(input())
s = [0] * n
w = [0] * n

for i in range(n):
    s[i], w[i] = map(int, input().split())
    
result = 0
recur(0, s)
print(result)