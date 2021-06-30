# 동물원
# https://www.acmicpc.net/problem/1309

n = int(input())

a = [[0] * 3 for _ in range(n + 1)]

no = 0
left = 1
right = 2

a[1][no] = 1
a[1][left] = 1
a[1][right] = 1

for i in range(2, n + 1):
    a[i][no] = (a[i - 1][no] + a[i - 1][left] + a[i - 1][right]) % 9901
    a[i][left] = (a[i - 1][no] + a[i - 1][right]) % 9901
    a[i][right] = (a[i - 1][no] + a[i - 1][left]) % 9901

print(sum(a[n]) % 9901)