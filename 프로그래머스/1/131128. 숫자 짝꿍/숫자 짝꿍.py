def solution(X, Y):
    answer = ""
    pair=[]
    #숫자 구성 0~9
    #딕셔너리로 비교하기
    X_dict={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    Y_dict={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    X=str(X)
    Y=str(Y)
    for x in X:
        if x in X_dict:
            X_dict[x]+=1
    
    for y in Y:
        if y in Y_dict:
            Y_dict[y]+=1
    # print(X_dict,Y_dict)
    #짝꿍 존재해야하는 건?
    #X,Y 짝꿍이 되는 것은  dictionary에 포함

    for key,value in X_dict.items():
        if value>=1 and Y_dict[key]>=1:
            match=min(value,Y_dict[key]) #반복횟수?
            for i in range(match):
                pair.append(key)
    # print(pair)
    
    if len(pair)==0:
        answer="-1"
    elif pair.count('0')==len(pair):
        
        answer="0"
    else:
        pair_int=[int(j) for j in pair]
        pair_int.sort(reverse=True) #내림차순 정렬
        for p in pair_int:
            answer+=str(p)

    return answer