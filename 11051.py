# 이항 계수 2
# https://www.acmicpc.net/problem/11051

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0] * (i + 1) for i in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1
    dp[i][i] = 1

for i in range(n + 1):
    for j in range(1, i):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 10007

print(dp[n][k])
