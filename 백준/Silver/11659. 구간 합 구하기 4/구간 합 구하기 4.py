#11659 구간 합 구하기 4
# 누적합

import sys

input=sys.stdin.readline

n,m=map(int,input().split())

k=[0]+list(map(int,input().split()))
a=[0]*(n+1)

for i in range(1,n+1):
    a[i]=a[i-1]+k[i]

for j in range(m):
    x,y=map(int,input().split())
    print(a[y]-a[x-1])
