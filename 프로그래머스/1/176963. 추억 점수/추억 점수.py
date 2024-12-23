def solution(name, yearning, photo):
    answer = []
    #name: key value:yearning 인 dict만들기
    dict={name: value for name,value in zip(name,yearning)}
    
    #photo길이에 대해서 방문하기
    for li in photo: #photo안쪽 요소 꺼내기기
        score=0
        for name in li:
             if dict.get(name):
                score+=dict.get(name)
        answer.append(score)
        
    return answer