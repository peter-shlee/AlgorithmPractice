# 상어 초등학교
# https://www.acmicpc.net/problem/21608

import sys
from collections import defaultdict

adjacent_idx = ((1, 0), (0, 1), (-1, 0), (0, -1))


def is_valid_idx(classroom, i, j):
    if 0 <= i < len(classroom) and 0 <= j < len(classroom[i]):
        return True

    return False


def check(classroom, i, j, friends):
    global adjacent_idx

    adjacent_students = []
    adjacent_best_friends_count = 0
    empty_seats_cnt = 0

    for idx in adjacent_idx:
        next_i = i + idx[0]
        next_j = j + idx[1]
        if is_valid_idx(classroom, next_i, next_j):
            if classroom[next_i][next_j] == 0:
                empty_seats_cnt += 1
            else:
                adjacent_students.append(classroom[next_i][next_j])

    for adjacent_student in adjacent_students:
        if adjacent_student in friends:
            adjacent_best_friends_count += 1

    return adjacent_best_friends_count, empty_seats_cnt


def find_seat(classroom, friends):
    answer_i = 0
    answer_j = 0
    max_adjacent_best_friends_cnt = -1
    max_empty_seats_cnt = -1

    for i in range(len(classroom)):
        for j in range(len(classroom[i])):
            if classroom[i][j] == 0:
                adjacent_best_friends_cnt, empty_seats_cnt = check(
                    classroom, i, j, friends)

                if adjacent_best_friends_cnt > max_adjacent_best_friends_cnt:
                    max_adjacent_best_friends_cnt = adjacent_best_friends_cnt
                    max_empty_seats_cnt = empty_seats_cnt
                    answer_i = i
                    answer_j = j
                elif adjacent_best_friends_cnt == max_adjacent_best_friends_cnt:
                    if empty_seats_cnt > max_empty_seats_cnt:
                        max_empty_seats_cnt = empty_seats_cnt
                        answer_i = i
                        answer_j = j

    return answer_i, answer_j



input = sys.stdin.readline

n = int(input())
classroom = [[0] * n for _ in range(n)]
num_of_students = n * n

best_friends = defaultdict(list)
for _ in range(num_of_students):
    s, *friends = map(int, input().split())
    best_friends[s] = friends
    i, j = find_seat(classroom, friends)
    classroom[i][j] = s

answer = 0
for i in range(n):
    for j in range(n):
        s = classroom[i][j]
        cnt, _ = check(classroom, i, j, best_friends[s])

        if cnt > 0:
            answer += 10 ** (cnt - 1)

print(answer)