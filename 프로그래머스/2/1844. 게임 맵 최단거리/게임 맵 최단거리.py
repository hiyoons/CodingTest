from collections import deque

def solution(maps):

    #user가 가능한 방향
    able_x=[-1,1,0,0]
    able_y=[0,0,-1,1]
    #방문 여부
    visited=[[False]*len(maps[0]) for _ in range(len(maps))]
    visited[0][0]=True
    #큐 선언 , 방문을 담은
    q=deque()
    q.append((0,0))
    #q가 비어있을 때까지 반복하기
    while q:
        q_y,q_x=q.popleft()
        #상하좌우에 대하여
        for i in range(4):
            qx=q_x+able_x[i]
            qy=q_y+able_y[i]
            #맵에 포함되어 있고
            if 0<=qx<len(maps[0]) and 0<=qy<len(maps) and maps[qy][qx]==1:
                #방문하지 않은 노드
                if visited[qy][qx]==False:
                    #큐에 insert
                    visited[qy][qx]=True #방문하고
                    q.append((qy,qx)) #큐에 삽입
                    maps[qy][qx]=maps[q_y][q_x]+1 #2가 된다
    if maps[len(maps)-1][len(maps[0])-1]==1:
        return -1
    else:
        return maps[len(maps)-1][len(maps[0])-1]
    
  