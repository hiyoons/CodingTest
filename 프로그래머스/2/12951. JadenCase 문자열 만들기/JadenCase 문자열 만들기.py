

def solution(s):
    answer = ''
    jadencase=s.split(' ')
    listlen=len(jadencase)
    for i in range(listlen):
        c=jadencase[i]
        if c:
            if c[0].isalpha():
                answer+=c[0].upper()+c[1:].lower()
            else :
                answer+=c[0]+c[1:].lower()
        else : 
             answer+=c
        if i!=listlen-1:
            answer+=' '
    
    return answer