def solution(a, b):
    res1=int(f'{a}{b}')
    res2=2*a*b
    if res1==res2:
        return res1
    else:
        return max(res1,res2)