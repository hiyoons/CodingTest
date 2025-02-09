answer=0
def dfs(numbers,index,calc,target):
    global answer
    if index==len(numbers):
        if calc==target:
            answer+=1
            return 
        else:
            return
    dfs(numbers,index+1,calc+numbers[index],target) 
    dfs(numbers,index+1,calc-numbers[index],target)             
    

def solution(numbers,target):
    global answer
    dfs(numbers,0,0,target)
    return answer