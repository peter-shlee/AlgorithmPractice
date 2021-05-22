# https://www.acmicpc.net/problem/11866
# 요세푸스 문제 0

n, k = list(map(int, input().split()))

nums = list(range(1, n + 1))
seq = []
next = 0

while len(nums):
    next = (next + k - 1) % len(nums)
    seq.append(nums[next])
    nums.remove(nums[next])

print("<", end="")
for n in seq:
    print(n, end="")
    if seq[len(seq) - 1] != n:
        print(", ", end="")
print(">", end="")
