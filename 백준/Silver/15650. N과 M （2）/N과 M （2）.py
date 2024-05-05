N,M = map(int,input().split())
res=[]

def backtrack_2(start):
   
    if len(res)==M:
         print(" ".join(map(str,res)))
         return
             
    for i in range(start,N+1):
        if i not in res:
            res.append(i)
            backtrack_2(i+1)
            res.pop()
             
backtrack_2(1)