def solution(num, arr1, arr2):
    decode = []
    arr1ToBin=[]
    arr2ToBin=[]
    decode=[]
    # or조건
    for i in range(len(arr1)):
        x=format(arr1[i],'b')
        while len(x)<num:
            x='0'+x
        arr1ToBin.append(x)
    for j in range(len(arr2)):
        y=format(arr2[j],'b')
        while len(y)<num:
            y='0'+y
        arr2ToBin.append(y)   
   
    for n in range(0,num):
        cal=''
        for m in range(0,num):
            if arr1ToBin[n][m]=='1' or arr2ToBin[n][m]=='1':
                cal+='#'
            else:
                cal+=' '
        decode.append(cal)
    return decode