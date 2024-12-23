def check(direct,x,y,k,obj):
    if direct=="W":
        for i in range(k+1):
            if obj[x][y-i]=="X":
                return False
        return True
    
    elif direct=="E":
        for i in range(k+1):
            if obj[x][y+i]=="X":
                return False
        return True
    elif direct=="N":
        for i in range(k+1):
            if obj[x-i][y]=="X":
                return False
        return True
    else:
        for i in range(k+1):
            if obj[x+i][y]=="X":
                return False
        return True
    

def solution(park, routes):
    
    x_start=0 #시작 위치 
    y_start=0
    obj=[["O"]*len(park[0]) for i in range(len(park))]
    
    for row in range(len(park)):
        for col in range(len(park[row])) :
            if park[row][col]=="S":
                x_start=row
                y_start=col
            elif park[row][col]=="X":
                obj[row][col]="X"
            else:
                continue
    print(x_start,y_start)
    print(obj)
    #routes 따라가기
    for rou in routes:
        d=rou.split()
        k=int(d[1])
        if d[0]=="W":
            if y_start-k>=0 and check("W",x_start,y_start,k,obj):
                print("W")
                y_start-= k
        elif d[0]=="E":
            if y_start+k<len(park[0]) and check("E",x_start,y_start,k,obj):
                print("E")
                y_start+=k 
        elif d[0]=="N":
            if x_start-k>=0 and check("N",x_start,y_start,k,obj):
                print("N")
                x_start-=k
        else:
            if x_start+k<len(park) and check("S",x_start,y_start,k,obj):
                print("S")
                x_start+=k
       
    
    return [x_start,y_start]