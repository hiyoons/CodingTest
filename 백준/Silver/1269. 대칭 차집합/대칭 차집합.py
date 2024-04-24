n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

set_a=set(a)
set_b=set(b)

res=len(set_a.difference(set_b))+len(set_b.difference(set_a))

print(res)