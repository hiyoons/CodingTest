import datetime


def solution(today, terms, privacies):
    answer = []
    today_parse=datetime.datetime.strptime(today,'%Y.%m.%d') #today 파싱'
    data_pos=1
    for priv in privacies:
        privDate=priv[:10]
        #privDate 파싱
        privDate_parse=datetime.datetime.strptime(privDate,'%Y.%m.%d') #모든 달 28일
        priv_year=privDate_parse.year
        priv_month=privDate_parse.month
        priv_day=privDate_parse.day
        
        endYear=priv_year
        endMonth=0
        endDay=priv_day
        privType=priv[11:] #타입
        
        for tr in terms:
            if privType==tr[0]:
                split_tr=tr.split()
                spend_month=int(split_tr[1])
                plusYear=(priv_month+spend_month)/12
                #정수가 아니면 plus하기
                if str(type(plusYear))!="<class 'int'>" and plusYear>1:
                    if (priv_month+spend_month)%12==0:
                        endYear+=int(plusYear)-1
                    else:
                        endYear+=int(plusYear)
                
                endMonth=(priv_month+spend_month)%12
                if endMonth==0:
                    endMonth=12
                    
                if priv_day>=2:
                    endDay=priv_day-1
                else:
                    if endMonth>1:
                        endMonth-=1
                    else:
                        endMonth=12
                    endDay=28
        endDate=datetime.datetime(endYear,endMonth,endDay)
        if endDate<today_parse:
            answer.append(data_pos)
        data_pos+=1
    return answer