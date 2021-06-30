# 오르막 수
# https://www.acmicpc.net/problem/11057

import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n = int(input())

dp = [[0] * n for _ in range(10)]

for i in range(10):
    dp[i][0] = 1

for i in range(1, n):
    for j in range(10):
        for k in range(j, 10):
            dp[j][i] += dp[k][i - 1]

answer = 0
for i in range(10):
    answer += dp[i][n - 1]
    answer %= 10007

print(answer)
