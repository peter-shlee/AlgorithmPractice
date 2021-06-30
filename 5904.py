# Moo 게임
# https://www.acmicpc.net/problem/5904

# s(k) = s(k - 1) * 2 + (k + 3)
# s(0) = 3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10*8)

def calc(s, k, n):
    if k == 0:
        if n == 1:
            print("m")
        else:
            print("o")

        return

    if n <= s[k - 1]:
        calc(s, k - 1, n)
    elif s[k - 1] < n <= s[k - 1] + (k + 3):
        if n - s[k - 1] == 1:
            print("m")
        else:
            print("o")
    else:
        calc(s, k - 1, n - (s[k - 1] + (k + 3)))
    

n = int(input())

s = [3]
k = 1
while True:
    s.append((s[k - 1] * 2) + (k + 3))
    if s[k] > n:
        break
    else:
        k += 1

calc(s, k, n)