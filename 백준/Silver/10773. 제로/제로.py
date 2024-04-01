k = int(input())
#스택 생성 ->리스트로 구현
stack =[]


for i in range(k):
    num=int(input())
    if num==0:
        stack.pop()
    else:
        stack.append(num)
        
print(sum(stack))