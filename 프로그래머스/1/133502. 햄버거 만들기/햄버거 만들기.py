def solution(ingredient):
    answer = 0
    burger=[]
    N = len(ingredient)
    for i in range(N):
        burger.append(ingredient[i])
        if burger[-4:]==[1,2,3,1]:
            answer+=1
            burger.pop()
            burger.pop()
            burger.pop()
            burger.pop()
    return answer