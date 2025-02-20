
def solution(s):
    answer = -1
    stack=[]
    
    for ch in s:
        if len(stack)>0 and stack[-1]==ch:
            stack.pop()
        else:
            stack.append(ch)
    
    if len(stack)==0:
        answer=1
    else:
        answer=0
        
    
    return answer