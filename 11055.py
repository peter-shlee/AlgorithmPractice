# 가장 큰 부분 수열
# https://www.acmicpc.net/problem/11055

import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = deepcopy(nums)

for i in range(1, n):
    for j in range(0, i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + nums[i])

print(max(dp))