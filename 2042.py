# https://www.acmicpc.net/problem/2042
# 구간 합 구하기

import sys

def init(left, right, node):

    if left == right:
        range_sums[node] = nums[left]
        return range_sums[node]
    
    mid = (left + right) // 2
    range_sums[node] = init(left, mid, node * 2) + init(mid + 1, right, node * 2 + 1)
    return range_sums[node]
    
def update(left, right, node, target_index, new_value):

    if target_index < left or right < target_index:
        return range_sums[node]

    if left == right:
        range_sums[node] = new_value
        return range_sums[node]

    mid = (left + right) // 2
    range_sums[node] = update(left, mid, node * 2, target_index, new_value) + update(mid + 1, right, node * 2 + 1, target_index, new_value)
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
    query_or_update, b, c = list(map(int, sys.stdin.readline().split()))

    if query_or_update == 2: # query
        print(query(1, N, 1, b, c))
    else: # update
        update(1, N, 1, b, c)
