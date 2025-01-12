#보물
import sys

n=sys.stdin.readline()
a=list(map(int,input().split()))
b=list(map(int,input().split()))
copy_a=a.copy()
copy_b=b.copy()
#a의 최대값,b의 최솟값 곱하고 계속 없애기
result1=0
result2=0
for i in range(int(n)):
    a_max=max(a)
    b_min=min(b)
    result1+=a_max*b_min
    a.remove(a_max)
    b.remove(b_min)
    
for j in range(int(n)):
    a_min=min(copy_a)
    b_max=max(copy_b)
    result2+=a_min*b_max
    copy_a.remove(a_min)
    copy_b.remove(b_max)
print(min(result1,result2))