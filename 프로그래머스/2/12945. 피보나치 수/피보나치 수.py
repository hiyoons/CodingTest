def fibo(n):
    d=[0]*100001
    d[0]=0
    d[1]=1
    for i in range(2,n+1):
        d[i]=d[i-1]+d[i-2]
    return d[i]
        
def solution(n):
    return fibo(n)%1234567