# https://www.acmicpc.net/problem/3085
# 사탕 게임

def check_row(board, i):
    prev = ""
    max_count = -1
    cur_count = 0
    for j in range(len(board[i])):
        if prev == board[i][j]:
            cur_count += 1
        else:
            if max_count < cur_count:
                max_count = cur_count
            cur_count = 1
            prev = board[i][j]
    
    if max_count < cur_count:
        max_count = cur_count
    
    return max_count

def check_col(board, i):
    prev = ""
    max_count = -1
    cur_count = 0
    for j in range(len(board)):
        if prev == board[j][i]:
            cur_count += 1
        else:
            if max_count < cur_count:
                max_count = cur_count
            cur_count = 1
            prev = board[j][i]
    
    if max_count < cur_count:
        max_count = cur_count
    
    return max_count

n = int(input())
board = []

for _ in range(n):
    board.append(list(input()))

answer = 0

# for i in range(n):
#     answer = max(answer, check_row(board, i))
#     answer = max(answer, check_col(board, i))

for i in range(n):
    for j in range(n):

        if j < n - 1 :
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            answer = max(answer, check_row(board, i))
            answer = max(answer, check_col(board, j))
            answer = max(answer, check_col(board, j + 1))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        if i < n - 1 :
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            answer = max(answer, check_col(board, j))
            answer = max(answer, check_row(board, i))
            answer = max(answer, check_row(board, i + 1))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(answer)
