x=[]
y=[]

for _ in range(3):
    n,m = map(int,input().split(" "))
    x.append(n)
    y.append(m)
dup=[]
if x[0]==x[1]:
    dup.append(x[2])
elif x[1]==x[2]:
    dup.append(x[0])
else:
    dup.append(x[1])
    
if y[0]==y[1]:
    dup.append(y[2])
elif y[1]==y[2]:
    dup.append(y[0])
else:
    dup.append(y[1])

print(*dup)