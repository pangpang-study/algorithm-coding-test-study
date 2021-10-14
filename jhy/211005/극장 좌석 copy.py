import sys

input = sys.stdin.readline

def fibonacci(n):
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

n = int(input())
m = int(input())

vip = [0] * (m + 1)

for i in range(1, m + 1):
    vip[i] = int(input())

vip.append(n + 1)

dp = [1, 1] + [0] * (n - 1)

result = 1

fibonacci(n)

for i in range(1, m + 2):
    length = vip[i] - vip[i - 1] - 1
    result *= dp[length]

print(result)