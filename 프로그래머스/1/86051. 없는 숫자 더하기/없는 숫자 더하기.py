def solution(numbers):
    answer = 0
    arr=[num for num in range(10) ]
    for i in arr:
        if i not in numbers:
            answer+=i
            
    
    return answer