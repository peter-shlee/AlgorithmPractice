# 2048 (Easy)
# https://www.acmicpc.net/problem/12100

import sys

input = sys.stdin.readline


def calc_new_line(line):
    new_line = []

    if len(line) == 0:
        return new_line

    prev_num = line.pop(0)
    while len(line) > 0:
        if line[0] == prev_num:
            new_line.append(prev_num * 2)
            line.pop(0)
            if len(line) == 0:
                prev_num = 0
                break
        else:
            new_line.append(prev_num)

        prev_num = line.pop(0)

    if prev_num != 0:
        new_line.append(prev_num)

    return new_line


def move_left(board):
    n = len(board)
    new_board = [[0] * n for i in range(n)]

    for i in range(n):
        num_in_line = []

        for j in range(n):
            if board[i][j] != 0:
                num_in_line.append(board[i][j])

        new_num_in_line = calc_new_line(num_in_line)

        for j in range(len(new_num_in_line)):
            new_board[i][j] = new_num_in_line[j]

    return new_board


def move_right(board):
    n = len(board)
    new_board = [[0] * n for i in range(n)]

    for i in range(n):
        num_in_line = []

        for j in range(n)[::-1]:
            if board[i][j] != 0:
                num_in_line.append(board[i][j])

        new_num_in_line = calc_new_line(num_in_line)

        for j in range(len(new_num_in_line)):
            new_board[i][n - 1 - j] = new_num_in_line[j]

    return new_board


def move_up(board):
    n = len(board)
    new_board = [[0] * n for i in range(n)]

    for j in range(n):
        num_in_line = []

        for i in range(n):
            if board[i][j] != 0:
                num_in_line.append(board[i][j])

        new_num_in_line = calc_new_line(num_in_line)

        for i in range(len(new_num_in_line)):
            new_board[i][j] = new_num_in_line[i]

    return new_board


def move_down(board):
    n = len(board)
    new_board = [[0] * n for i in range(n)]

    for j in range(n):
        num_in_line = []

        for i in range(n)[::-1]:
            if board[i][j] != 0:
                num_in_line.append(board[i][j])

        new_num_in_line = calc_new_line(num_in_line)

        for i in range(len(new_num_in_line)):
            new_board[n - 1 - i][j] = new_num_in_line[i]

    return new_board


def calc(board, moved_count):
    max_value = 0

    if moved_count == 5:
        max_value = max(map(max, board))
        return max_value

    new_board = move_left(board)
    max_value = max(max_value, calc(new_board, moved_count + 1))

    new_board = move_right(board)
    max_value = max(max_value, calc(new_board, moved_count + 1))

    new_board = move_up(board)
    max_value = max(max_value, calc(new_board, moved_count + 1))

    new_board = move_down(board)
    max_value = max(max_value, calc(new_board, moved_count + 1))

    return max_value


def main():
    n = int(input())
    board = []

    for i in range(n):
        new_line = list(map(int, input().split()))
        board.append(new_line)

    answer = calc(board, 0)
    print(answer)


main()
