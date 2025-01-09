import heapq
import sys
heap=[]
n=int( sys.stdin.readline())
cnt=0
#자연수이면 x값 insert

for i in range(n):

    k = int( sys.stdin.readline())

    if k==0:
        if len(heap)==0:
            print(0)
        else:
            print( heapq.heappop((heap)))
        cnt+=1
    
        if cnt==n: 
            break
    else:
        heapq.heappush(heap,k)
