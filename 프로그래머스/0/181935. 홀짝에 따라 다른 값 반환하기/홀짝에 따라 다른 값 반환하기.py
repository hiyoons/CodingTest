def solution(n):
    answer = 0
    if n%2==0:
        for k in range(1,n+1):
            if k%2==0:
                answer+=k*k
    else:
        for k in range(1,n+1):
            if k%2!=0:
                answer+=k
    return answer