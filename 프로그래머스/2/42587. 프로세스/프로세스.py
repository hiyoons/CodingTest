

def solution(priorities, location):
    answer = 0
    process = [(index,p) for index,p in enumerate(priorities)]#튜플로 저장
    
    while True:
        current=process.pop(0)
        if any(current[1]<p[1] for p in process):
            process.append(current)
        else:
            answer += 1
            if current[0] == location:
                return answer
    
    return answer