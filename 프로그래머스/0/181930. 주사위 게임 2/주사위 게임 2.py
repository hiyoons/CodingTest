def solution(a, b, c):
    answer = 0
    if a==b:
        if a==c:
            answer=(a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
        else: #ab는 같고 c는 다름
            answer=(a+b+c)*(a**2+b**2+c**2)
    else:
        #a,b는 다름 
        if a==c or b==c:
            answer=(a+b+c)*(a**2+b**2+c**2)
        else:
            answer=a+b+c
    return answer