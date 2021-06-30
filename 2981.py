# 검문
# https://www.acmicpc.net/problem/2981

import sys

input = sys.stdin.readline

def getGCD(a, b):
    if a < b:
        a ,b = b, a
    
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b

    return b

def getDivisors(num):
    divisors = []

    for i in range(1, int(num**(0.5)) + 1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num // i)

    divisors.append(num)
    divisors = list(set(divisors))
    divisors.sort()
    return divisors

n = int(input())
numbers = []
difference = []

for _ in range(n):
    numbers.append(int(input()))

numbers.sort()

for i in range(len(numbers) - 1):
    difference.append(numbers[i + 1] - numbers[i])

gcd = difference[0]
for i in range(1, len(difference)):
    gcd = getGCD(gcd, difference[i])

divisors = getDivisors(gcd)
divisors.pop(0)
print(*divisors)
