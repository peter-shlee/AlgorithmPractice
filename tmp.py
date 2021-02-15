n = int(input())
num_list = list(map(int,input().split()))

if n==1:
    print(1)
    exit()

dp = [-1]*n
dp[0] = 1
result = 1
for i in range(1,n):
    max_val = 0
    for j in range(i):
        if num_list[i] > num_list[j]:
            max_val = max(max_val, dp[j])

    dp[i] = max_val+1
    result = max(result,dp[i])

print(result)
