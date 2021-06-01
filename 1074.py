# Z
# https://www.acmicpc.net/problem/1074

import sys

imput = sys.stdin.readline

n, r, c = map(int, input().split())
answer = 0

while n > 0:
    half_len = 2 ** (n - 1)
    quarter_size = half_len ** 2

    right = False
    bottom = False
    if r >= half_len: bottom = True
    if c >= half_len: right = True

    if not right and not bottom: # 왼쪽 위
        pass
    elif right and not bottom: # 오른쪽 위
        answer += quarter_size * 1
        c -= half_len
    elif not right and bottom: # 왼쪽 아래
        answer += quarter_size * 2
        r -= half_len
    else: # 오른쪽 아래
        answer += quarter_size * 3
        c -= half_len
        r -= half_len

    n -= 1

print(answer)