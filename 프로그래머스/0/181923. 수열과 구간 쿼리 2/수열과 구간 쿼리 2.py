def solution(arr, queries):
    answer = [] 
    for s,e,k in queries:
        q=[]
        for i in range(s,e+1):
            if arr[i]>k:
                q.append(arr[i]) 
        if len(q)>=1:
            answer.append(min(q))
        else:
            answer.append(-1)
        
             
            
    return answer