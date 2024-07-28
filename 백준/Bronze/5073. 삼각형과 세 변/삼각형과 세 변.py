end_tr=[0,0,0]
while True:
    triangle = list(map(int,input().split()))
    triangle.sort()
    if triangle==end_tr:
        break
    else:
        if triangle[2] >= triangle[0]+triangle[1]:
            print("Invalid")
        else:
            if triangle[0]==triangle[1]:
                if triangle[0]!=triangle[2]:
                    print("Isosceles")
                else:
                    print("Equilateral")
            elif triangle[0]==triangle[2]:
                if triangle[0]!=triangle[1]:
                    print("Isosceles")
                else:
                    print("Equilateral")
            elif triangle[1]==triangle[2]:
                if triangle[0]!=triangle[1]:
                    print("Isosceles")
                else:
                    print("Equilateral")
            else:
                print("Scalene")