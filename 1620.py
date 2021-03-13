# https://www.acmicpc.net/problem/1620
# 나는야 포켓몬 마스터 이다솜

import sys

n, m = list(map(int, input().split()))

pocketmon_dict = dict()

for i in range(n):
    pocketmon_dict[i + 1] = sys.stdin.readline().rstrip()

inverse_dict = {v: k for k, v in pocketmon_dict.items()}

for _ in range(m):
    query = sys.stdin.readline().rstrip()
    if query.isdigit():
        print(pocketmon_dict[int(query)])
    else:
        print(inverse_dict[query])