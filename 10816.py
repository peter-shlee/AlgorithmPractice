# https://www.acmicpc.net/problem/10816
# 숫자 카드 2

from collections import Counter

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
query = list(map(int, input().split()))

num_count = Counter(nums)

for q in query:
    print(num_count[q], end=" ")
