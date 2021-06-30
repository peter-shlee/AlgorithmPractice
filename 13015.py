# https://www.acmicpc.net/problem/13015
# 별 찍기 23

def print_stars(n):
    print("*" * n, end="")

def print_sep_stars(n):
    print(f"*{' ' * (n - 2)}*", end="")

def print_space(n):
    print(" " * n, end="")

n = int(input())

# 위쪽 반 출력
for i in range(1, n):
    print(" " * (i - 1), end="")

    if i == 1:
        print_stars(n)
    else:
        print_sep_stars(n)

    print_space((n - i) * 2 - 1)

    if i == 1:
        print_stars(n)
    else:
        print_sep_stars(n)

    print()

# 가운데 줄 출력
print(" " * (n - 1), end="")
print(f"*{' ' * (n - 2)}*{' ' * (n - 2)}*")

# 아래쪽 반 출력
for i in range(n + 1, 2 * n):
    i = 2 * n - i

    print(" " * (i - 1), end="")

    if i == 1:
        print_stars(n)
    else:
        print_sep_stars(n)

    print_space((n - i) * 2 - 1)

    if i == 1:
        print_stars(n)
    else:
        print_sep_stars(n)

    print()