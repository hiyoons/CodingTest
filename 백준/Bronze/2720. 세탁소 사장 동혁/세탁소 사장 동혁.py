t=int(input())
change=[25,10,5,1]
for _ in range(t):
    c=int(input())
    cnt=[]
    for i in range(len(change)):
        cnt.append(c//change[i])
        c%=change[i]
    print(*cnt)
