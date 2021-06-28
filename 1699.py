# 제곱수의 합 -> pypy3
# https://www.acmicpc.net/problem/1699

import sys

input = sys.stdin.readline

n = int(input())

dp = [987654321] * (n + 1)

dp[1] = 1

for i in range(2, n + 1):
    sqrt = i ** (0.5)
    if sqrt == int(sqrt):
        dp[i] = 1
        continue

    sqrt = int(sqrt)
    for j in range(1, sqrt + 1):
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)

print(dp[n])