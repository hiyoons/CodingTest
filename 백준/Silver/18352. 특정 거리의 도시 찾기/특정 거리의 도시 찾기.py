#최단 거리 -> bfs
import sys
from collections import deque
n,m,k,x=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]
distance=[0]*(n+1)
visited=[False]*(n+1)


for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)




#bfs 구현
def bfs(x):
    answer=[]
    queue=deque([x])
    visited[x]=True
    distance[x]=0
    
    while queue:
        x=queue.popleft()
        #현재 위치에서 네 방향으로 위치 확인
        for i in graph[x]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)
                distance[i]=distance[x]+1
                if distance[i]==k:
                    answer.append(i)
    if len(answer)==0:
            answer.append(-1)
    return answer


res=bfs(x)
res.sort()
for i in res:
    print(i,end='\n')