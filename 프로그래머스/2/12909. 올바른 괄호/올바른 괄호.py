def solution(s):
    answer = True
    stk=[]
    
    for ch in s:
        if ch=="(":
            stk.append(ch)
        else:
            if stk and stk[-1]=="(":
                stk.pop()
            else:
                stk.append(ch)
    if stk:
        answer=False
    
    return answer