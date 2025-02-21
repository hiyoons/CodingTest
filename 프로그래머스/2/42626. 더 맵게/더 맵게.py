import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #heap구조로 변형
    while len(scoville)>=2:
        min=heapq.heappop(scoville)
        if min>=K:
            return answer
        else:
            second_min=heapq.heappop(scoville)
            heapq.heappush(scoville,min+second_min*2)
        answer+=1
    min=heapq.heappop(scoville)
    if min<K:
        answer=-1
    return answer