# https://www.acmicpc.net/problem/10999
# 구간 합 구하기 2

import sys

def init(left, right, node):

    if left == right:
        range_sums[node] = nums[left]
        return range_sums[node]
    
    mid = (left + right) // 2
    range_sums[node] = init(left, mid, node * 2) + init(mid + 1, right, node * 2 + 1)
    return range_sums[node]
    
def update(left, right, node, target_left, target_right, num_add):

    if target_right < left or right < target_left:
        return range_sums[node]

    if left == right:
        range_sums[node] = range_sums[node] + num_add
        return range_sums[node]

    mid = (left + right) // 2
    range_sums[node] = update(left, mid, node * 2, target_left, target_right, num_add) + update(mid + 1, right, node * 2 + 1, target_left, target_right, num_add)
    return range_sums[node]

def query(left, right, node, target_left, target_right):

    if target_right < left or right < target_left:
        return 0

    if target_left <= left and right <= target_right:
        return range_sums[node]

    mid = (left + right) // 2
    return query(left, mid, node * 2, target_left, target_right) + query(mid + 1, right, node * 2 + 1, target_left, target_right)
    
N, M, K = list(map(int, sys.stdin.readline().split()))
nums = [0]

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

range_sums = [0] * (4 * N)
init(1, N, 1)

for _ in range(M + K):
    input_nums = list(map(int, sys.stdin.readline().split()))

    if input_nums[0] == 2: # query
        print(query(1, N, 1, input_nums[1], input_nums[2]))
    else: # update
        update(1, N, 1, input_nums[1], input_nums[2], input_nums[3])
