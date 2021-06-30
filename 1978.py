# https://www.acmicpc.net/problem/1978
# 소수 찾기

n = int(input())
input_nums = list(map(int, input().split()))
max_num = max(input_nums)
primes = set()
nums = set(range(2, max_num + 1))

while len(nums) > 0:
    next_prime = min(nums)
    primes.add(next_prime)
    nums.remove(next_prime)

    none_prime = next_prime ** 2
    while none_prime <= max_num:
        if none_prime in nums:
            nums.remove(none_prime)
        none_prime += next_prime

answer = 0
for num in input_nums:
    if num in primes:
        answer += 1

print(answer)