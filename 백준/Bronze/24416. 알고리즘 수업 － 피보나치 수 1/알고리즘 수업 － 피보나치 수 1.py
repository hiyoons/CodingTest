num=int(input())

def fibo(n):
    global cnt_fibo
    if n==1 or n==2:
         cnt_fibo+=1
         return 1
    else:
        
        return fibo(n-1)+fibo(n-2)
def dynamic(n):
    global cnt_dyn
    d=[0]*(n+1)
    d[0]=1
    d[1]=1
    for i in range(3,n+1):
        
        d[i]=d[i-1]+d[i-2]
        cnt_dyn+=1
    return d[n]

cnt_fibo=0
cnt_dyn=0
fibo(num)
dynamic(num)

print(cnt_fibo,cnt_dyn)
