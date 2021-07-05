# 상범 빌딩
# https://www.acmicpc.net/problem/6593

import sys

input = sys.stdin.readline

adjacent_indices = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def is_valid_index(building, l, r, c):
    if l < 0 or r < 0 or c < 0:
        return False

    if len(building) <= l:
        return False

    if len(building[l]) <= r:
        return False

    if len(building[l][r]) <= c:
        return False

    return True


while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break

    s = []
    e = []

    building = []
    for i in range(l):
        floor = []
        for j in range(r):
            floor.append(list(input().strip()))
            if "S" in floor[j]:
                s = (i, j, floor[j].index("S"))
            elif "E" in floor[j]:
                e = (i, j, floor[j].index("E"))

        building.append(floor)
        input()

    answer = -1
    queue = [(s[0], s[1], s[2], 0)]
    break_flag = False
    building[s[0]][s[1]][s[2]] = "#"
    while len(queue) > 0 and not break_flag:
        cur_l, cur_r, cur_c, count = queue.pop(0)

        for adjacent_index in adjacent_indices:
            next_l = adjacent_index[0] + cur_l
            next_r = adjacent_index[1] + cur_r
            next_c = adjacent_index[2] + cur_c

            if is_valid_index(building, next_l, next_r, next_c):
                if building[next_l][next_r][next_c] == ".":
                    building[next_l][next_r][next_c] = "#"
                    queue.append((next_l, next_r, next_c, count + 1))
                elif building[next_l][next_r][next_c] == "E":
                    answer = count + 1
                    break_flag = True
                    break
    
    if answer == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {answer} minute(s).")
