n,t=map(int,input().split())

totaltime=0
result=0

work=list(map(int,input().split()))

for i in range(n):
    totaltime+=work[i]
    if totaltime > t:
        break
    else:
        result+=1

print(result)

    