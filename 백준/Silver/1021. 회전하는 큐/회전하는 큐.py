from collections import deque

n,m=map(int,input().split())
position=list(map(int,input().split()))
dq=deque([i for i in range(1,n+1)])

answer=0

for pos in position:
    while len(dq)>0:
        if dq[0]==pos:
            dq.popleft()
            break
        else:
            if dq.index(pos) <=len(dq)//2:
                dq.rotate(-1)
                answer+=1
            else:
                dq.rotate(1)
                answer+=1
   
print(answer)