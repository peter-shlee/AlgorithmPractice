# 01타일
# https://www.acmicpc.net/problem/1904

import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
    exit()

dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746

print(dp[n])