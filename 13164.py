n, k = list(map(int, input().split()))
kids = list(map(int, input().split()))
dif = []
for i in range(1, n):
    dif.append((i - 1, kids[i] - kids[i - 1]))

dif.sort(key= lambda x: x[1], reverse=True)

cut_idx = []
for i in range(k - 1):
    cut_idx.append(dif[i][0])
cut_idx.sort()

answer = 0
start = 0
for i in range(len(cut_idx)):
    end = cut_idx[i]
    answer += kids[end] - kids[start]
    start = end + 1
end = len(kids) - 1
answer += kids[end] - kids[start]

print(answer)
