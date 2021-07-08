# DSLR
# https://www.acmicpc.net/problem/9019

## pypy3 -> 통과
## python3 -> 시간초과

import sys
from collections import deque

input = sys.stdin.readline

def solve():
    a, b = map(int, input().split())

    queue = deque()
    queue.append((a, []))

    visited = [False] * 10000
    visited[a] = True

    answer = None

    while len(queue) > 0:
        c, w = queue.popleft()
        lc = list(str(c))
        z = ["0"] * (4 - len(lc))

        lc = z + lc

        c_d = c * 2 % 10000

        c_s = c - 1
        if c_s == -1:
            c_s = 9999

        c_l = int("".join(lc[1:] + [lc[0]]))

        c_r = int("".join([lc[3]] + lc[:3]))

        if not visited[c_d]:
            visited[c_d] = True
            if c_d == b:
                answer = w + ["D"]
                print(*answer, sep="")
                return
            queue.append((c_d, w + ["D"]))

        if not visited[c_s]:
            visited[c_s] = True
            if c_s == b:
                answer = w + ["S"]
                print(*answer, sep="")
                return
            queue.append((c_s, w + ["S"]))

        if not visited[c_l]:
            visited[c_l] = True
            if c_l == b:
                answer = w + ["L"]
                print(*answer, sep="")
                return
            queue.append((c_l, w + ["L"]))

        if not visited[c_r]:
            visited[c_r] = True
            if c_r == b:
                answer = w + ["R"]
                print(*answer, sep="")
                return
            queue.append((c_r, w + ["R"]))


t = int(input())

for _ in range(t):
    solve()
