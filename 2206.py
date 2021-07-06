# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206

import sys
from collections import deque

input = sys.stdin.readline

adjacent_indices = ((1, 0), (-1, 0), (0, 1), (0, -1))


def is_valid_index(graph, r, c):
    if r < 0 or c < 0:
        return False

    if len(graph) <= r:
        return False

    if len(graph[r]) <= c:
        return False

    return True


n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().strip())))

count_0 = [[987654321] * m for _ in range(n)]
count_1 = [[987654321] * m for _ in range(n)]

queue = deque()
if graph[0][0] == 0:
    queue.append((0, 0, False))
else:
    queue.append((0, 0, True))
    
count_0[0][0] = 1
while len(queue) > 0:
    cur_r, cur_c, broken_flag = queue.popleft()

    for adjacent_index in adjacent_indices:
        next_r = cur_r + adjacent_index[0]
        next_c = cur_c + adjacent_index[1]

        if is_valid_index(graph, next_r, next_c):
            if graph[next_r][next_c] == 0:
                if broken_flag:
                    if count_0[next_r][next_c] > count_1[cur_r][cur_c] + 1 and count_1[next_r][next_c] > count_1[cur_r][cur_c] + 1:
                        count_1[next_r][next_c] = count_1[cur_r][cur_c] + 1
                        queue.append((next_r, next_c, broken_flag))
                else:
                    if count_0[next_r][next_c] == 987654321:
                        count_0[next_r][next_c] = count_0[cur_r][cur_c] + 1
                        queue.append((next_r, next_c, broken_flag))
            else:
                if not broken_flag and count_1[next_r][next_c] == 987654321:
                    count_1[next_r][next_c] = count_0[cur_r][cur_c] + 1
                    queue.append((next_r, next_c, True))

answer = min(count_0[n - 1][m - 1], count_1[n - 1][m - 1])
if answer == 987654321:
    answer = -1

print(answer)
# print(*count_0, sep="\n")
# print()
# print(*count_1, sep="\n")