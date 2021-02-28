# https://www.acmicpc.net/problem/2609
# 최대공약수와 최소공배수

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

def LCM(a, b):
    gcd = GCD(a, b)
    return gcd * a // gcd * b // gcd

a, b = list(map(int, input().split()))
print(GCD(a, b))
print(LCM(a, b))
