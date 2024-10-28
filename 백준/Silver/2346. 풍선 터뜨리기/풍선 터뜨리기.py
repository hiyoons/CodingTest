from collections import deque
import sys

n=int(input())
ballons_init=[i+1 for i in range(n)]
balldeque=deque(ballons_init)

#음수->양수로 양수->음수로 
paper=list(map(int,sys.stdin.readline().split()))
paper_rotate=[x for x in paper]

#풍선 터뜨리기
popballon=[]

move_ballon=balldeque.copy()
k=move_ballon.popleft()
popballon.append(k)
while move_ballon:
   if paper_rotate[k-1]>0:
       move_ballon.rotate(-paper_rotate[k-1]+1)
   else:
       move_ballon.rotate(-paper_rotate[k-1])
    
   k=move_ballon.popleft()
   popballon.append(k)
for pops in popballon:
    print(pops,end=' ')   