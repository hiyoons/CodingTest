def solution(answers):
    answer = []
    f_person=[1,2,3,4,5]
    s_person=[2,1,2,3,2,4,2,5]
    t_person=[3,3,1,1,2,2,4,4,5,5]
    
    f_cnt=0
    s_cnt=0
    t_cnt=0
    
    #answers길이만큼 늘리기

    for i in range(len(answers)):
        index=i%len(f_person)
        if f_person[index]==answers[i]:
            f_cnt+=1
    for i in range(len(answers)):
        index=i%len(s_person)
        if s_person[index]==answers[i]:
            s_cnt+=1
    for i in range(len(answers)):
        index=i%len(t_person)
        if t_person[index]==answers[i]:
            t_cnt+=1
            
    if f_cnt==s_cnt and s_cnt==t_cnt:
        answer=[1,2,3]
    elif f_cnt>s_cnt:
        if f_cnt>t_cnt:
            answer.append(1)
        elif f_cnt==t_cnt:
            answer=[1,3]
        else:
            answer=[3]
    elif f_cnt==s_cnt:
        if f_cnt>t_cnt:
            answer=[1,2]
        else:
            answer=[3]
    else: #f_cnt<s_cnt
        if s_cnt>t_cnt:
            answer=[2]
        elif s_cnt==t_cnt:
            answer=[2,3]
        else:
            answer=[3]
        
    return answer