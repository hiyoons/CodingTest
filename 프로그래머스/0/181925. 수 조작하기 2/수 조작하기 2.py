def solution(numLog):
    answer = ''
    nm={1:"w",-1:"s",10:"d",-10:"a"}
    for idx in range(len(numLog)-1):
        res=numLog[idx+1]-numLog[idx]
        answer+=nm[res]
    return answer