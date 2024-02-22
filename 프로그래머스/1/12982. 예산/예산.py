def solution(d, budget):
    answer = 0
    pos_d=0
    i=0
    #전체합 구하기 
    #for i in range(len(d)):
    #    sum+=d[i]
    
    d.sort()
    if sum(d)<=budget:
        answer=len(d)
    else:
        #정렬
        while pos_d<=budget:
            pos_d+=d[i]
            i+=1
            
        answer=i-1
        
    return answer