# 평범한 배낭
# https://www.acmicpc.net/problem/12865

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

items = []

for _ in range(n):
    items.append(list(map(int, input().split())))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    item_value = items[i - 1][1]
    item_weight = items[i - 1][0]
    for j in range(k + 1):
        if j - item_weight >= 0:
            dp[i][j] = max(dp[i - 1][j - item_weight] + item_value, dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])