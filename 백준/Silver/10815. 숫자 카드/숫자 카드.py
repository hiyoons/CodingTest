n=int(input())
#list로 입력받기
sang=list(map(int,input().split())) #리스트로 입력받기
#list를 set(집합으로 변환)
set_sang=set(sang)

m=int(input())
comp=list(map(int,input().split())) #비교해야되는 수 입력 받기
set_comp=set(comp)

inter_sang=set_sang.intersection(set_comp) #교집합 저장

res = [1 if i in inter_sang else 0 for i in comp]

print(" ".join(map(str,res)))