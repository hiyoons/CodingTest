from itertools import combinations_with_replacement
n,m=map(int,input().split())
arr=[i+1 for i in range(n)]

for item in combinations_with_replacement(arr,m):
    ch=list(item)
    print(*ch)