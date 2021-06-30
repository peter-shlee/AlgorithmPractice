# 안전영역
# https://www.acmicpc.net/problem/2468

def canGo(board, i, j):
    if i < 0 or j < 0:
        return False

    if len(board) <= i or len(board) <= j:
        return False

    if board[i][j] <= 0:
        return False
    
    return True

def dfs(board, i, j):
    board[i][j] = -1

    if canGo(board, i, j + 1):
        dfs (board, i, j + 1)
    if canGo(board, i + 1, j):
        dfs (board, i + 1, j)
    if canGo(board, i, j - 1):
        dfs (board, i, j - 1)
    if canGo(board, i - 1, j):
        dfs (board, i - 1, j)


def check(board):
    count = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] > 0:
                count += 1
                dfs(board, i, j)

    return count

import sys
import copy

sys.setrecursionlimit(100000000)
input = sys.stdin.readline

n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

answer = 1
height = 0
while True:
    height += 1

    for i in range(n):
        for j in range(n):
            if board[i][j] == height:
                board[i][j] = -1

    tmp_board = copy.deepcopy(board)
    count = check(tmp_board)
    if count == 0:
        break

    answer = max(answer, count)

print(answer)