# 이친수
# https://www.acmicpc.net/problem/2193

import sys

input = sys.stdin.readline

n = int(input())

dp = [[0] * 2 for _ in range(n + 1)]
dp[1][0] = 1
dp[1][1] = 1

for i in range(2, len(dp)):
    dp[i][0] = sum(dp[i - 1])
    dp[i][1] = dp[i - 1][0]

print(dp[n][1])