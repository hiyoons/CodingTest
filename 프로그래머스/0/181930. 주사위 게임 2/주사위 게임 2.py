def solution(a, b, c):
    answer =a+b+c
    listToSet=set([a,b,c])
    if len(listToSet)==1:
        answer*=(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif len(listToSet)==2:
        answer*=(a**2+b**2+c**2)
    else:
        return answer
    return answer