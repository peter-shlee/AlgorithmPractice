# https://www.acmicpc.net/problem/2992
# 크면서 작은 수

from collections import Counter

x = input()
counter = Counter(x)
answer = 0
same_counter_flag = False

n = sum(dict(counter).values())

num = int(x) + 1
num_counter = Counter(str(num))
while (sum(dict(num_counter).values())) == n:
    same_counter_flag = True
    for k, v in dict(num_counter).items():
        if counter[k] != v:
            same_counter_flag = False
            break

    if same_counter_flag:
        answer = num
        break
    num += 1
    num_counter = Counter(str(num))

print(answer)