# https://www.acmicpc.net/problem/11727
# 2xn 타일링 2

n = int(input())

memo = [0] * 1001

memo[1] = 1
memo[2] = 3
for i in range(3, n + 1):
    memo[i] = (memo[i - 1] + memo[i - 2] * 2) % 10007

print(memo[n])