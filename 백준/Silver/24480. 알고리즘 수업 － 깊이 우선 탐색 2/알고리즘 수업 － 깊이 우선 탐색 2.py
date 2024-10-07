from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(10 ** 8)


def dfs(start):
    global count
    visited[start]=True
    answer[start]=count
    for node in graph[start]:
        if visited[node]==False:
            count+=1
            dfs(node)

#dfs code 
n,m,r=map(int,input().split())



graph=[[] for i in range(n+1)]
visited=[False]*(n+1)#방문여부확인
answer = [0] * (n+1) #방문순서

for i in range(m):
   u,v=map(int,input().split())
   graph[u].append(v)
   graph[v].append(u)

    
    
#내림차순 정렬
for i in range(n+1):
    graph[i].sort(reverse=True)#true내림차순


count=1
dfs(r)
print("\n".join(map(str,answer[1:])))
    