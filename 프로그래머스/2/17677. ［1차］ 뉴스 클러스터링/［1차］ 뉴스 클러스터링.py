

def clearStr(li):
    only_str=[]
    for i in range(len(li)):
        if li[i].isalpha()==True:
            only_str.append(li[i].upper())
            
    return only_str

def doubleList(str):
    strlist=[]
    for i in range(len(str)-1):
        twoset=str[i]+str[i+1]
        strlist.append(twoset)
    return strlist

def solution(str1, str2):
    answer = 0

    #다중집합 만들기
    first_doubleList=doubleList(str1)
    second_doubleList=doubleList(str2)
   

    #알파벳으로만 이뤄진 것 
    first_alpha=clearStr(first_doubleList)
    second_alpha=clearStr(second_doubleList)

  

    same=set(first_alpha) & set(second_alpha)
    hap=set(first_alpha) | set(second_alpha)

    cnt_same=sum([min(first_alpha.count(i),second_alpha.count(i)) for i in same])
    cnt_haps=sum([max(first_alpha.count(i),second_alpha.count(i)) for i in hap])

    if cnt_same==0 and cnt_haps==0:
        jaka=1
    else:
        jaka=cnt_same/cnt_haps
    answer=int(jaka*65536)
    
    
    return answer
