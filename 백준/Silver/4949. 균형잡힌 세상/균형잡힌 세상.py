import sys 

def balance(ch):
    stack=[]
    for c in ch:
        if c=='(' or c=='[':
            stack.append(c)
        elif c==')':
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop() 
            else:
                stack.append(c)
        elif c==']':
            if len(stack)!=0 and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(c)
    
    if len(stack)==0:
        print("yes")
    else:
        print("no")
        

              
                
while True:
    a=sys.stdin.readline().rstrip() #strip으로 개행문자 없애기
    if a=='.':
        break   
    else:
        balance(a)
