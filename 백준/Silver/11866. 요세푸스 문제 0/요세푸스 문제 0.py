from collections import deque
answer=[]
n,k=map(int,input().split())
arr=[i+1 for i in range(n)]
q=deque(arr)
for i in range(n):
    q.rotate(-(k-1))
    pop=q.popleft()
    answer.append(pop)
print('<',end='')
print(*answer,sep=', ',end='')
print('>')
