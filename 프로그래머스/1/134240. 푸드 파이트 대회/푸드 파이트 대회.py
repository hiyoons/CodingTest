def solution(food):
    answer = ''
    a_half=''
    f_dict={}
    for i in range(1,len(food)):
        key=i
        if food[i]%2==0:
            f_dict[i]=food[i]
        else:
            f_dict[i]=food[i]-1
    
    for keys in f_dict.keys():
        h_value=f_dict[keys]//2
        a_half+=str(keys)*h_value
    
    b_half=a_half[::-1]
    answer=a_half+'0'+b_half
    return answer