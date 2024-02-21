n, m = map(int, input().split())
bucket = [b + 1 for b in range(n)]

for c in range(m):
    i, j = map(int, input().split())
    tmp = bucket[i - 1 : j]
    tmp.reverse()
    bucket[i - 1 : j] = tmp


print(" ".join(map(str, bucket)))