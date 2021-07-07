# 스타트링크
# https://www.acmicpc.net/problem/5014

import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

dp = [-1] * (f + 1)
dp[s] = 0
queue = deque()
queue.append(s)

while len(queue) > 0:
    c = queue.popleft()

    down_index = c - d
    if down_index > 0:
        if dp[down_index] == -1:
            dp[down_index] = dp[c] + 1
            queue.append(down_index)
            
    
    up_index = c + u
    if up_index <= f:
        if dp[up_index] == -1:
            dp[up_index] = dp[c] + 1
            queue.append(up_index)

if dp[g] == -1:
    print("use the stairs")
else:
    print(dp[g])