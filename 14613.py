# https://www.acmicpc.net/problem/14613
# 너의 티어는?

comb = []
for i in range(21):
    comb.append([-1] * (i + 1))

def calc_comb(a, b):
    if comb[a][b] == -1:
        c = 1
        p = 1
        for i in range(1, b + 1):
            c *= a - (i - 1)
            p *= i

        comb[a][b] = c // p
        comb[a][a - b] = comb[a][b]
    return comb[a][b]

w, l, d = list(map(float, input().split()))

rank = [0] * 5

for n_w in range(20 + 1):
    for n_l in range(20 - n_w + 1):
        score = 2000 + n_w * 50 - n_l * 50
        index = score // 500 - 2
        rank[index] += ((w ** n_w) * (l ** n_l) * (d ** (20 - n_w - n_l))) * calc_comb(20, n_w) * calc_comb(20 - n_w, n_l)

for i in range(len(rank)):
    print(format(rank[i]/sum(rank), ".8f"))
