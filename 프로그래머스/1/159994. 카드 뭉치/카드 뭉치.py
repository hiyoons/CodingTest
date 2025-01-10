def solution(cards1, cards2, goal):
    answer = 'Yes'
    for card in goal:
        if card in cards1:
            if card!=cards1.pop(0):
                
                return 'No'
        elif card in cards2:
            if card!=cards2.pop(0):
                
                return 'No'
        else:
            continue        
       
    return answer