# https://www.acmicpc.net/problem/11050
# 이항 계수 1

n, k = list(map(int, input().split()))

answer = 1
for i in range(k):
    answer *= n
    n -= 1

for i in range(2, k + 1):
    answer //= i

print(answer)
