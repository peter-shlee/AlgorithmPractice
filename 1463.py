# test_accuracy
# 1로 만들기

n = int(input())
memoization = [0] * (n + 1)

for x in range(2, n + 1):
    min_count = 9876543210
    if x % 3 == 0:
        if memoization[x // 3] < min_count:
            min_count = memoization[x // 3]
    
    if x % 2 == 0:
        if memoization[x // 2] < min_count:
            min_count = memoization[x // 2]
    
    if memoization[x - 1] < min_count:
        min_count = memoization[x - 1]

    memoization[x] = min_count + 1

print(memoization[n])