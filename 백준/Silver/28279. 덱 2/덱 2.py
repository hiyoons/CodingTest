from collections import deque
import sys

n=int(input())
newdeque=deque()
for i in range(n):
    cmd=list(map(int,sys.stdin.readline().split()))
    sizeofdeque=len(newdeque)
    if len(cmd)==1:
        if  cmd[0]==3:
            if newdeque: # not empty
                print(newdeque.popleft())
            else:
                 print(-1)
        elif cmd[0]==4:
            if newdeque:
             print(newdeque.pop())
            else:
             print(-1)
        elif cmd[0]==5:
             print(sizeofdeque)
        elif cmd[0]==6:
            if newdeque:
                print(0)
            else:
                print(1)
        elif cmd[0]==7:
            if newdeque:
                print(newdeque[0])
            else:
             print(-1)
        else:
            if newdeque:
             print(newdeque[sizeofdeque-1])
            else:
                print(-1)
    else:
        if cmd[0]==1:
            newdeque.appendleft(int(cmd[1]))
        elif cmd[0]==2:
            newdeque.append(int(cmd[1]))
    