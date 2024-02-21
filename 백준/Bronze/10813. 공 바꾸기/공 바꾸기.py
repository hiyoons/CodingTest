n, m = map(int, input().split())

bucket = [b + 1 for b in range(n)]
# 1부터 n까지 값을 가진 길이가 n인 리스트 생성


for k in range(0, m):
    i, j = map(int, input().split())
    bucket[i - 1], bucket[j - 1] = bucket[j - 1], bucket[i - 1]


print(" ".join(map(str, bucket)))