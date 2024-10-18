n=int(input())

for i in range(0,n):
    stack=[]
    s=input()
    result="YES"
    for ch in s:
        if ch=="(":
            stack.append(ch)
        elif ch==")":
            if stack:
                stack.pop()
            else:
                result="NO"
                break
    if not stack and result=="YES":
        print("YES")
    elif stack or result=="NO":
        print("NO")
    
        

        