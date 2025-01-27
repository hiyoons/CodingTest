import sys
n=int(input())
book={}

for i in range(n):
    title=sys.stdin.readline()
    if title not in book.keys():
        book[title]=0
    else:
        book[title]+=1
#value가 최대값인 것을 찾기
li=[k for k,v in book.items() if max(book.values())==v]

if len(li)==1:
    print(li[0])
else:
    sor=sorted(li)
    print(sor[0])    