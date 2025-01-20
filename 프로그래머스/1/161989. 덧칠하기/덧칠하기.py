def solution(n, m, section):
    answer = 0
    roller=0
    for s in section:
        if s>roller:
            answer+=1
            roller=s+m-1 # m : 롤러의 길이
            
                         
    return answer