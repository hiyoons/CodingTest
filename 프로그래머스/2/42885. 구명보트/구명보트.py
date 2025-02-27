def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    sum=0
    cnt=0
    i=0
    j=len(people)-1
    while i<j:   
        if people[i]+people[j]>=limit:
            if len(people)>0:
                people.pop(i)
                i+=1
        else:
            if i>=0:
                people.pop(i)
                i+=1
            if j<len(people):
                people.pop(j)
                j-=1
        answer+=1
    return answer