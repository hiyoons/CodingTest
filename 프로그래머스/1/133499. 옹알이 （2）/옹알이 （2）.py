def solution(babbling):
    answer = 0
    able=['aya','ma','woo','ye']
    notable=['ayaaya','mama','woowoo','yeye']
    
    for word in babbling:
        for i in range(4): #word에 연속인 값이 포함되어있다면 *로 replace하기
            if notable[i] in word:#word에 notable이 포함되어있지 않을때 replace가능?
                word=word.replace(notable[i],'*')
                break
        for a in able:
            word=word.replace(a,' ')
            print(word)
        if word.isspace():
                answer+=1
    return answer