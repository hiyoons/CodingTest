import sys
import heapq

n=int(input())
#최대 힙 
max_heap=[]

#n개의 줄에 연산의 정보
#x가 0이면 배열에서 가장 큰 값 출력&제거
for i in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        #가장 큰 값 출력&제거
        #배열이 비어있는 경우
        if len(max_heap)==0:
            print(0)
        else:
            print(heapq.heappop(max_heap)[1])
    else:
        heapq.heappush(max_heap,(-x,x))
