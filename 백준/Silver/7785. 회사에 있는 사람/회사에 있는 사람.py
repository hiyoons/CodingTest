n=int(input())
company={}
#list로 입력받기
for i in range(n):
    key,value=input().split()
    company[key]=value

res=[k for k,v in company.items() if v=='enter']
print('\n'.join(sorted(res,reverse=True)))