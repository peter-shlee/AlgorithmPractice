# 카드 구매하기
# https://www.acmicpc.net/problem/11052

import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i - j >= 0:
            dp[i] = max(dp[i], dp[i - j] + p[j - 1])

print(dp[n])