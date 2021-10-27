import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

vip = []

for i in range(m):
    vip.append(int(input()))

dp = [0 for _ in range(n+1)] 
dp[1] = 1

if 2 in vip or 1 in vip:
    dp[2] = 1
else:
    dp[2] = 2



for i in range(3,n+1):
    if i in vip or i-1 in vip :
        dp[i] = dp[i-1]
    else:
        if i-2 in vip: 
            dp[i] = dp[i-1] *2
        else:
            dp[i] = dp[i-1] + dp[i-2]

print(dp[-1])