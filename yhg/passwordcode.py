import sys
input = sys.stdin.readline

result = 0
num = input().rstrip()
dp = [0] * (len(num)+1)
dp[0] = 1
for i in range(1, len(num)+1):
    if num[i-1] == 0 and i-1 == 0:
        print(0)
        exit()

    else:
        if 1 <= int(num[i-1]) <= 9:
            dp[i] += dp[i-1]

        if i != 1 and 10 <= int(num[i-2]) * 10 + int(num[i-1]) <= 26:
            dp[i] += dp[i-2]

print(dp[-1] % 1000000)
