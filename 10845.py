# https://www.acmicpc.net/problem/10845
# 큐

from collections import deque
import sys

dq = deque()

n = int(input())
for _ in range(n):
    query = list(sys.stdin.readline().split())
    if query[0] == "push":
        num = int(query[1])
        dq.append(num)
    elif query[0] == "pop":
        if len(dq):
            print(dq.popleft())
        else:
            print(-1)
    elif query[0] == "front":
        if len(dq):
            print(dq[0])
        else:
            print(-1)
    elif query[0] == "back":
        if len(dq):
            print(dq[len(dq) - 1])
        else:
            print(-1)
    elif query[0] == "size":
        print(len(dq))
    elif query[0] == "empty":
        if len(dq):
            print(0)
        else:
            print(1)
