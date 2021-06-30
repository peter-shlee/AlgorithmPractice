# https://www.acmicpc.net/problem/14648
# 쿼리 맛보기

def seq_sum(seq, start, end):
    total = 0
    for i in range(start, end + 1):
        total += seq[i]
    return total

n, q = list(map(int, input().split()))

seq = [0]
seq += list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        print(seq_sum(seq, query[1], query[2]))
        seq[query[1]], seq[query[2]] = seq[query[2]], seq[query[1]]
    else:
        print(seq_sum(seq, query[1], query[2]) - seq_sum(seq, query[3], query[4]))
