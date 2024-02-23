def solution(t, p):
    cnt = 0
    answer = 0
    while cnt <= len(t) - len(p):
        number = ""
        for i in range(0, len(p)):
            number += t[i + cnt]
        if int(number) <= int(p):
            answer += 1
        cnt += 1
    
            
            
    return answer