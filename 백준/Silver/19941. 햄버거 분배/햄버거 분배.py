n,k=map(int,input().split()) #n=식탁길이,거리가 k이하인 햄버거 eat
position=list(input()) #위치 문자열열


answer=0
for p in range(len(position)):
    if position[p]=="P": #사람이 있다면 해당 인덱스에서 +K~-K까지가 햄버거 범위
        left=max(p-k,0)
        right=min(p+k+1,n)
        for j in range(left,right): #테이블 범위
            if position[j]=="H":
                position[j]="o"
                answer+=1
                break
        
print(answer)