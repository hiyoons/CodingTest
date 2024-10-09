import sys

def starPattern(n):
    init=["***","* *","***"]
    
    if n==3:
        return init
    a_pattern=list()
    star=starPattern(n//3)
    b_pattern=list()
    
    for s in star:
        a_pattern.append(s*3)
   
    for s in star:
       b_pattern.append(s+' '*(n//3)+s)

    
    return a_pattern+b_pattern+a_pattern

n=int(sys.stdin.readline())
print('\n'.join(starPattern(n)))
    