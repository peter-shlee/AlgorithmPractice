# 숨바꼭질 3
# https://www.acmicpc.net/problem/13549

maximum = 100000
minimum = 0

n, k = map(int, input().split())
queue = [(n, 0)]
visited = [0] * (maximum + 1)


while len(queue) != 0:
    current_position, current_time = queue.pop(0)
    visited[current_position] = 1

    if current_position == k:
        print(current_time)
        break

    nn = current_position * 2
    while nn <= maximum:
        if visited[nn] == 0:
            visited[nn] = 1
            queue.append((nn, current_time))
            nn *= 2
        else:
            break
        
    if current_position - 1 >= minimum:
        if visited[current_position - 1] == 0:
            visited[current_position - 1] = 1
            queue.append((current_position - 1, current_time + 1))

    if current_position + 1 <= maximum:
        if visited[current_position + 1] == 0:
            visited[current_position + 1] = 1
            queue.append((current_position + 1, current_time + 1))

