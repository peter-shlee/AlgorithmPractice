# https://www.acmicpc.net/problem/1037
# 약수

n = int(input())
nums = list(map(int, input().split()))

min_num = min(nums)
max_num = max(nums)

print(min_num * max_num)