# 숨바꼭질
# https://www.acmicpc.net/problem/1697

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [-1] * max(2 * (k + 2), n + 1)
queue = deque()
queue.append(n)
dp[n] = 0

while len(queue) > 0:
    c = queue.popleft()

    if c == k:
        break

    if k < c:
        if dp[c - 1] == -1:
            dp[c - 1] = dp[c] + 1
            queue.append(c - 1)
    else:
        if c - 1 >= 0:
            if dp[c - 1] == -1:
                dp[c - 1] = dp[c] + 1
                queue.append(c - 1)

        if c * 2 - k < k - (c + 1):
            if dp[c * 2] == -1:
                dp[c * 2] = dp[c] + 1
                queue.append(2 * c)

        if dp[c + 1] == -1:
            dp[c + 1] = dp[c] + 1
            queue.append(c + 1)

print(dp[k])