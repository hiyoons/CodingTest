import sys

n,m=map(int,input().split())
pokemon=dict()
#n개의 줄에 입력
for i in range(n):
    pokemon[i+1]=sys.stdin.readline().rstrip()

reverse_pokemon=dict(map(reversed,pokemon.items()))
#문제 맞추기
for _ in range(m):
    q=sys.stdin.readline().rstrip()
    if q.isdigit():
        print(pokemon[int(q)])
    else:
        print(reverse_pokemon[q])