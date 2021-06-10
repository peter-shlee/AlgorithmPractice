# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

import sys
from itertools import permutations

input = sys.stdin.readline

def calc(a, operators):
    result = a[0]

    for i in range(0, len(operators)):
        if operators[i] == "+":
            result += a[i + 1]
        elif operators[i] == "-":
            result -= a[i + 1]
        elif operators[i] == "*":
            result *= a[i + 1]
        else:
            if result < 0:
                result = -(-result // a[i + 1])
            else:
                result //= a[i + 1]

    return result

n = int(input())
a = list(map(int, input().split()))

plus, minus, multiplication, division = map(int, input().split())
operators = []
operators.extend(["+"] * plus)
operators.extend(["-"] * minus)
operators.extend(["*"] * multiplication)
operators.extend(["/"] * division)

min_ans = 9876543210
max_ans = -9876543210
operator_permutations = set(permutations(operators, len(operators)))
for operators in operator_permutations:
    result = calc(a, operators)
    if result > max_ans:
        max_ans = result

    if result < min_ans:
        min_ans = result

print(max_ans)
print(min_ans)