def solution(code):
    answer = ''
    mode=0 #시작 MODE=0 #abc1abc1abc
    for idx in range(len(code)):
        if mode==0:
            if code[idx]!='1':
                if idx%2==0: 
                    answer+=code[idx]
            if code[idx]=='1':
                mode=1
        else:#mode=1
            if code[idx]!='1': 
                if idx%2!=0:
                    answer+=code[idx]
            if code[idx]=='1':
                mode=0
    if len(answer)==0:
        answer='EMPTY'
    return answer