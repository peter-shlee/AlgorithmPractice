# 문자열 판별
# https://www.acmicpc.net/problem/16500

import sys

def check(s, idx, a, dp):
    if idx == len(s):
        return True

    for i in range(len(a)):
        word = a[i]
        next_idx = idx + len(word)
        if next_idx > len(s):
            continue
        if s[idx:next_idx] == word and dp[i][idx] == 0:
            dp[i][idx] = 1
            if check(s, next_idx, a, dp):
                return True

    return False

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

s = input()[:-1]
n = int(input())
a = []
for _ in range(n):
    a.append(input()[:-1])

dp = [[0] * len(s) for _ in range(n)]

if check(s, 0, a, dp):
    print(1)
else:
    print(0)
