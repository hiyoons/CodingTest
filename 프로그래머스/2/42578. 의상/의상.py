import math

def solution(clothes):
    answer = 0
    clot_dict={}
    combi_init=1
    for i in range(len(clothes)):
        types=clothes[i][1]
        if types not in clot_dict:
            clot_dict[types]=1
        else:
            clot_dict[types]+=1
    if len(clot_dict)>1:
        for key in clot_dict.keys():
            combi_init*=(clot_dict[key]+1)
        answer=combi_init-1
    else:
        for key,value in clot_dict.items():
            answer+=value
    return answer