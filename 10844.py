# 쉬운 계단 수
# https://www.acmicpc.net/problem/10844

import sys

input = sys.stdin.readline

n = int(input())

dp = [[0] * (n + 1) for _ in range(10)]
for i in range(1, 10):
    dp[i][1] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j != 0:
            dp[j][i] = (dp[j][i] + dp[j - 1][i - 1]) % 1000000000
        if j != 9:
            dp[j][i] = (dp[j][i] + dp[j + 1][i - 1]) % 1000000000

answer = 0
for i in range(10):
    answer = (dp[i][n] + answer) % 1000000000

print(answer)