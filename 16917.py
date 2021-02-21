# https://www.acmicpc.net/problem/16917
# 양념 반 후라이드 반

import sys
A, B, C, X, Y = list(map(int, sys.stdin.readline().split()))

answer = 0

if A > 2 * C:
    A = 2 * C

if B > 2 * C:
    B = 2 * C

p = min(X, Y)
answer += (X - p) * A
answer += (Y - p) * B

if 2 * C < A + B:
    answer += p * C * 2
else:
    answer += p * (A + B)

print(answer)