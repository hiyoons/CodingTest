import sys
import heapq

input=sys.stdin.readline
INF=int(sys.maxsize)

n,m=map(int,input().split())
seem=list(map(int,input().split()))
backdoor=[[] for _ in range(n)] #각 노드 정보 담기
distance=[INF]*(n)
#간선 정보 입력받기
for _ in range(m):
    a,b,t=map(int,input().split())
    backdoor[a].append((b,t))
    backdoor[b].append((a,t))
#다익스트라 알고리즘
def dijkstra(start):
    q=[]
    #시작 노드는 0, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0
    
    while q:
        dist,now=heapq.heappop(q)
        #처리된 적 없는 것
        if distance[now]<dist: #큐의 비용이 현재 노드 보다 크면
            continue
        
        #현재 노드와 인접한 노드 확인
        for i in backdoor[now]:
            cost=dist+i[1]
            #현재 노드를 거쳐서 다른 노드로 가는 거리가 더 짧고 시야에 보이지 않을 때
            if cost < distance[i[0]] and seem[now]!=1:
                distance[i[0]]=cost #갱신
                heapq.heappush(q,(cost,i[0]))
               
dijkstra(0)

if distance[n-1]==INF:
    print(-1)  
else:
    print(distance[n-1])