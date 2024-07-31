def solution(sizes):
    answer = 0
    max_w=1
    max_h=1
    
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            w=sizes[i][0]
            h=sizes[i][1]
        else:
            w=sizes[i][1]
            h=sizes[i][0]
        if w>max_w :
            max_w=w
        if h>max_h:
            max_h=h
    answer = max_w * max_h
    return answer