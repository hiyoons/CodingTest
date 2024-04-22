n,m = map(int,input().split())
s=dict()

count=0

for i in range(n):
    w = input()
    s[w]=True

for _ in range(m):
    ch=input()
    if ch in s.keys():
        count+=1

print(count)