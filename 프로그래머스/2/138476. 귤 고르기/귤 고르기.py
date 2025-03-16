def solution(k, tangerine):
    answer = 0
    ta={}
    for i in tangerine:
        try: 
            ta[i]+=1
        except: 
            ta[i]=1
    tanger_sort=sorted(ta.items(),key=lambda x:x[1],reverse=True)
    tanger=dict(tanger_sort)
    tan_list=list(tanger.values())
    sum=0
    for i in range(len(tan_list)):
        if sum<k:
            sum+=tan_list[i]
            answer+=1
    return answer