# https://www.acmicpc.net/problem/16112
# 5차 전직

from queue import PriorityQueue

n, k = list(map(int, input().split()))
exp = list(map(int, input().split()))
pq = PriorityQueue()

for e in exp:
    pq.put(e)

answer = 0
stone_count = 0
while not pq.empty():
    answer += stone_count * pq.get()
    stone_count += 1

print(answer)
