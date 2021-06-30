# 별 찍기 - 10
# https://www.acmicpc.net/problem/2447

def set_pattern(n, board, x, y, star_flag):
    next_n = n // 3

    if n == 1:
        board[y][x] = star_flag
        return

    for i in range(3):
        for j in range(3):
            if i * j == 1:
                set_pattern(next_n, board, x + j * next_n, y + i * next_n, False)
            else:
                set_pattern(next_n, board, x + j * next_n, y + i * next_n, star_flag)

def print_pattern(board):
    for i in range(len(board)):
        
        for j in range(len(board[i])):
            if board[i][j]:
                print("*", end="")
            else:
                print(" ", end="")

        print()

n = int(input())

board = [[False] * n for _ in range(n)]
set_pattern(n, board, 0, 0, True)
print_pattern(board)