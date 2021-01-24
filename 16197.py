# https://www.acmicpc.net/problem/16197
# 두 동전

from collections import deque
from enum import IntEnum

class Direction(IntEnum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

class TwoCoinPositions:
    def __init__(self, coin_1_y:int, coin_1_x:int, coin_2_y:int, coin_2_x:int):
        self.coin_1 = CoinPosition(coin_1_y, coin_1_x)
        self.coin_2 = CoinPosition(coin_2_y, coin_2_x)

    def set_position(self, coin_1_y:int, coin_1_x:int, coin_2_y:int, coin_2_x:int):
        self.set_coin_1_position(coin_1_y, coin_1_x)
        self.set_coin_2_position(coin_2_y, coin_2_x)

    def set_coin_1_position(self, coin_1_y:int, coin_1_x:int):
        self.coin_1_y = coin_1_y
        self.coin_1_x = coin_1_x

    def set_coin_2_position(self, coin_2_y:int, coin_2_x:int):
        self.coin_2_y = coin_2_y
        self.coin_2_x = coin_2_x


class CoinPosition:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x

def check_fall_from_board(board, y: int, x: int):
    if y >= len(board) or y < 0: 
        return True
    if x >= len(board[0]) or x < 0: 
        return True
    return False

def check_can_move(board, y: int, x: int):
    if board[y][x] == ".":
        return True
    else:
        return False

def get_order_to_move(board, two_coin_positions: TwoCoinPositions, direction: Direction) -> list:
    # 움직일 순서대로 CoinPosition 객체를 리스트에 넣어 리턴
    order = []
    if direction == Direction.LEFT:
        if two_coin_positions.coin_1.x < two_coin_positions.coin_2.x:
            order.append(two_coin_positions.coin_1)
            order.append(two_coin_positions.coin_2)
        else:
            order.append(two_coin_positions.coin_2)
            order.append(two_coin_positions.coin_1)

    elif direction == Direction.RIGHT:
        if two_coin_positions.coin_1.x < two_coin_positions.coin_2.x:
            order.append(two_coin_positions.coin_2)
            order.append(two_coin_positions.coin_1)
        else:
            order.append(two_coin_positions.coin_1)
            order.append(two_coin_positions.coin_2)

    elif direction == Direction.DOWN:
        if two_coin_positions.coin_1.y < two_coin_positions.coin_2.y:
            order.append(two_coin_positions.coin_1)
            order.append(two_coin_positions.coin_2)
        else:
            order.append(two_coin_positions.coin_2)
            order.append(two_coin_positions.coin_1)

    else:
        if two_coin_positions.coin_1.y < two_coin_positions.coin_2.y:
            order.append(two_coin_positions.coin_2)
            order.append(two_coin_positions.coin_1)
        else:
            order.append(two_coin_positions.coin_1)
            order.append(two_coin_positions.coin_2)

    return order


n, m = list(map(int, input().split()))
board = []

for i in range(n):
    new_line = list(input())
    board.append(new_line)

coin_positions = []
for y, line in enumerate(board):
    for x, position in enumerate(line):
        if position == "o":
            coin_positions.append([x, y])

bfs_queue = deque([])
bfs_queue.append(TwoCoinPositions(coin_positions[0][0], coin_positions[0][1], coin_positions[1][0], coin_positions[1][1]))

while (len(bfs_queue) > 0):
    cur_coin_position = bfs_queue.popleft()
    print(bfs_queue)

    fall_count = 0
    if check_fall_from_board(board, cur_coin_position.coin_1.y + 1, cur_coin_position.coin_1.x):
        fall_count += 1
    if check_fall_from_board(board, cur_coin_position.coin_2.y + 1, cur_coin_position.coin_2.x):
        fall_count += 1
    if fall_count == 1:
        break
    elif fall_count == 2:
        pass
    else:
        need_to_check_next = False
        order_to_move = get_order_to_move(board, cur_coin_position, Direction.UP)
        next_coin_positions = []
        for coin_position in order_to_move:
            if check_fall_from_board(board, coin_position.y + 1, coin_position.x):
                need_to_check_next = True
                next_coin_positions.append([coin_position.y + 1, coin_position.x])
        if need_to_check_next:
            bfs_queue.append(TwoCoinPositions(next_coin_positions[0], next_coin_positions[1], next_coin_positions[2], next_coin_positions[3]))
                
                

    fall_count = 0
    if check_fall_from_board(board, cur_coin_position.coin_1.y - 1, cur_coin_position.coin_1.x):
        fall_count += 1
    if check_fall_from_board(board, cur_coin_position.coin_2.y - 1, cur_coin_position.coin_2.x):
        fall_count += 1
    if fall_count == 1:
        break
    elif fall_count == 2:
        pass
    else:
        need_to_check_next = False
        order_to_move = get_order_to_move(board, cur_coin_position, Direction.UP)
        next_coin_positions = []
        for coin_position in order_to_move:
            if check_fall_from_board(board, coin_position.y - 1, coin_position.x):
                need_to_check_next = True
                next_coin_positions.append([coin_position.y - 1, coin_position.x])
        if need_to_check_next:
            bfs_queue.append(TwoCoinPositions(next_coin_positions[0], next_coin_positions[1], next_coin_positions[2], next_coin_positions[3]))

    fall_count = 0
    if check_fall_from_board(board, cur_coin_position.coin_1.y, cur_coin_position.coin_1.x + 1):
        fall_count += 1
    if check_fall_from_board(board, cur_coin_position.coin_2.y, cur_coin_position.coin_2.x + 1):
        fall_count += 1
    if fall_count == 1:
        break
    elif fall_count == 2:
        pass
    else:
        need_to_check_next = False
        order_to_move = get_order_to_move(board, cur_coin_position, Direction.UP)
        next_coin_positions = []
        for coin_position in order_to_move:
            if check_fall_from_board(board, coin_position.y, coin_position.x + 1):
                need_to_check_next = True
                next_coin_positions.append([coin_position.y, coin_position.x + 1])
        if need_to_check_next:
            bfs_queue.append(TwoCoinPositions(next_coin_positions[0], next_coin_positions[1], next_coin_positions[2], next_coin_positions[3]))

    fall_count = 0
    if check_fall_from_board(board, cur_coin_position.coin_1.y, cur_coin_position.coin_1.x - 1):
        fall_count += 1
    if check_fall_from_board(board, cur_coin_position.coin_2.y, cur_coin_position.coin_2.x - 1):
        fall_count += 1
    if fall_count == 1:
        break
    elif fall_count == 2:
        pass
    else:
        need_to_check_next = False
        order_to_move = get_order_to_move(board, cur_coin_position, Direction.UP)
        next_coin_positions = []
        for coin_position in order_to_move:
            if check_fall_from_board(board, coin_position.y, coin_position.x - 1):
                need_to_check_next = True
                next_coin_positions.append([coin_position.y, coin_position.x - 1])
        if need_to_check_next:
            bfs_queue.append(TwoCoinPositions(next_coin_positions[0], next_coin_positions[1], next_coin_positions[2], next_coin_positions[3]))

print("complete")