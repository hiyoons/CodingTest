n = int(input())
li = list(map(int, input().split()))
set_li = sorted(list(set(li)))
dict = {set_li[i]: i for i in range(len(set_li))}
for d in li:
    print(dict[d], end=" ")