n=int(input())
x=[]
y=[]
for _ in range(n):
    x1,y1=map(int,input().split(" "))
    x.append(x1)
    y.append(y1)

width=max(x)-min(x)
height=max(y)-min(y)

print(width*height)