# https://www.acmicpc.net/problem/2201
# 이친수 찾기

k = 0
dp = [[-1] * 10000000 for i in range(2)]
num = [False] * 10000
length = 0


def getInput():
    global k
    global length
    k = int(input()) - 1


def solve():
    global length

    max_index = 0
    while True:
        max_index += 1
        for i in range(0, len(num)):
            num[i] = False
        num[0] = True
        if dfs(1, max_index, True):
            length = max_index
            break


def dfs(current_index, max_index, prev_one):
    global dp
    global k
    n = 0

    if k == 0:
        return True

    if max_index == current_index:
        k -= 1
        dp[0][current_index] = 1
        if not prev_one:
            dp[1][current_index] = 1
        return False

    if prev_one:
        if dp[0][current_index] != -1 and k - dp[0][current_index] > 0 :
            k -= dp[0][current_index]
            return False
    else:
        if dp[0][current_index] != -1 and  dp[1][current_index] != -1 and k - dp[0][current_index] - dp[1][current_index] > 0 :
            k -= dp[0][current_index] + dp[1][current_index]
            return False


    if dfs(current_index + 1, max_index, False):
        return True
    dp[0][current_index] = dp[0][current_index + 1]

    if not prev_one:
        num[current_index] = True
        if dfs(current_index + 1, max_index, True):
            return True
        num[current_index] = False
        dp[1][current_index] = dp[0][current_index + 1] + dp[1][current_index + 1]

    return False


if __name__ == "__main__":
    getInput()
    solve()
    for i in range(0, length):
        if num[i]:
            print(1, end="")
        else:
            print(0, end="")
    print()