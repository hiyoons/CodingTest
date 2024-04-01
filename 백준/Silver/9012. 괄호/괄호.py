k = int(input())
#스택 생성 ->리스트로 구현

for i in range(k):
    stack =[]
    vps=True
    s = input()
    
    for ch in s:
        if ch=='(':
            stack.append('(')
        if ch==')':
            if stack:
                stack.pop()
            elif not stack:
                vps=False
                break
    if not stack and vps:
        print('YES')
    elif stack or not vps:
        print("NO")
    