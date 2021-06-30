# https://www.acmicpc.net/problem/1543
# 문서 검색

string = input()
target_string = input()
answer = 0

start_index = string.find(target_string)
while start_index != -1:
    string = string[start_index + len(target_string):]
    answer += 1
    start_index = string.find(target_string)

print(answer)