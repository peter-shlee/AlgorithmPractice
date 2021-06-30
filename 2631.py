# 줄세우기
# https://www.acmicpc.net/problem/2631

import sys

input = sys.stdin.readline


def lis(ary):
    dp = [0] * len(ary)
    dp[0] = 1

    for i in range(1, len(ary)):
        prev_max = 0
        for j in range(0, i):
            if (ary[j] < ary[i]):
                prev_max = max(prev_max, dp[j])
        dp[i] = prev_max + 1

    return max(dp)


n = int(input())
children = []
for _ in range(n):
    children.append(int(input()))

answer = len(children) - lis(children)
print(answer)
