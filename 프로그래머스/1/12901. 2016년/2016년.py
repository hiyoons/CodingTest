import datetime
#윤년 2월 29일 
def solution(a, b):
    days=['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer=days[datetime.date(2016,a,b).weekday()]
    return answer