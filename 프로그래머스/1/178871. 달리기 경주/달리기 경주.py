now=dict()


def solution(players, callings):
    rank=0
    #players로 딕셔너리 만들기
    for p in players:
        now[p]=rank
        rank+=1
         # {"mumu":1,"soe":2,"poe":3,"kai":4,"mine":5}
    for call in callings:
        change_value=now[call] # 4
        front=players[change_value-1]
        now[call]-=1
        now[front]+=1
        players[change_value-1],players[change_value]=players[change_value],players[change_value-1]

    return players
