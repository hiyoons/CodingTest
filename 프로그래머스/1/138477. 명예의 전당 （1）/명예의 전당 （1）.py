def solution(k, score):
    #범위 3<=k<=100
    #score길이 7<=score의 길이<=1000
    hallofFame=[]
    answer=[]
    lenofScore=len(score)
    #초기 k일까지 모든 출연가수 목록 기재
    if k<lenofScore:
        
        for i in range(0,k):
            hallofFame.append(score[i])
            answer.append(min(hallofFame))
        
        for j in range(k,lenofScore):
            if score[j]>min(hallofFame):
                idx=hallofFame.index(min(hallofFame))
                del hallofFame[idx]
                hallofFame.append(score[j])
            answer.append(min(hallofFame))
    else:
        for i in range(0,lenofScore):
            hallofFame.append(score[i])
            answer.append(min(hallofFame))
  
    return answer