# https://www.acmicpc.net/problem/4375
# 1

while True:
    try:
        n = int(input())
    except Exception:
        break
    
    answer = 1
    r = 1 % n
    while r != 0:
        r = (r * 10 + 1) % n
        answer += 1

    print(answer)
    