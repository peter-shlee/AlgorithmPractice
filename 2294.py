# 동전 2
# https://www.acmicpc.net/problem/2294

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [987654321] * (k + 1)
dp[0] = 0

for i in range(len(dp)):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i - coin] + 1, dp[i])

if dp[k] == 987654321:
    dp[k] = -1
print(dp[k])