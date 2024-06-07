def solution(numbers):
    answer = set()
    #서로 다른 두개 뽑기 
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            answer.add(numbers[i]+numbers[j])
    answer=sorted(answer)
    answer=list(answer)
    return answer