triangle=list(map(int,input().split()))
triangle.sort()
tri_round=0
without_max=triangle[0]+triangle[1]
if triangle[2] >= without_max:
    tri_round=2*without_max-1
else:
    tri_round=sum(triangle)
print(tri_round)