def solution(a, b):
    res1=str(a)+str(b)
    res2=str(b)+str(a)
    return int(max(res1,res2))