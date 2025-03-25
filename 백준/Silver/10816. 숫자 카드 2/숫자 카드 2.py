from collections import defaultdict
import sys

n=input()
sang_card=list(map(int,sys.stdin.readline().split()))
sang_hash=defaultdict(int)
for s in sang_card:
    sang_hash[int(s)]+=1

m=int(input())
number_card=list(map(int,sys.stdin.readline().split()))
    
result=[]
for num in number_card:
    if sang_hash.get(num) is None:
        result.append(0)
    else:
        result.append(sang_hash.get(num))
    
print(*result)