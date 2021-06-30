# https://www.acmicpc.net/problem/2630
# 색종이 만들기

def cut(paper, start_y, end_y, start_x, end_x, color_count):

    color = check(paper, start_y, end_y, start_x, end_x)
    if color != -1:
        color_count[color] += 1
        return

    mid_y, mid_x = (start_y + end_y) // 2, (start_x + end_x) // 2

    cut(paper, start_y, mid_y, start_x, mid_x, color_count)
    cut(paper, start_y, mid_y, mid_x + 1, end_x, color_count)
    cut(paper, mid_y + 1, end_y, start_x, mid_x, color_count)
    cut(paper, mid_y + 1, end_y, mid_x + 1, end_x, color_count)

def check(paper, start_y, end_y, start_x, end_x):
    color = paper[start_y][start_x]
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            if color != paper[y][x]:
                return -1

    return color


n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

color_count = [0, 0]
cut(paper, 0, n - 1, 0, n - 1, color_count)
print(color_count[0])
print(color_count[1])
