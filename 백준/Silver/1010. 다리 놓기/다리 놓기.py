test= int(input())
result=1
mod=1

def factorial(k):
    fact=1
    for i in range(1,k+1):
        fact*=i
    return fact
def nCr(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))

for _ in range(test):
    n,m = map(int,input().split())
    print(nCr(m,n))