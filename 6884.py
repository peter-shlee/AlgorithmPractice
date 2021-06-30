# https://www.acmicpc.net/problem/6884
# 소수 부분 수열

import sys
import math

def is_primary(n):
    if n < 2:
        return False

    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            return False

    return True

num_of_test_case = int(input())

for _ in range(num_of_test_case):
    end_flag = False
    seq = list(map(int, sys.stdin.readline().split()))[1:]

    for n in range(2, len(seq) + 1):
        for i in range(len(seq)):
            if i + n >= len(seq):
                break

            sum = 0
            for j in range(i, i + n):
                sum += seq[j]
            
            if is_primary(sum):
                end_flag = True
                print(f"Shortest primed subsequence is length {n}:", end="")
                for j in range(i, i + n):
                    print(f" {seq[j]}", end="")
                print()
                break

        if end_flag:
            break
    
    if end_flag:
        continue
    print("This sequence is anti-primed.")

