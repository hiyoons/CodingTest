import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
    str = input()
    li.append(str)

set_list = list(set(li))


# 변형 o 반환값 x
set_list.sort()
set_list.sort(key=len)

for j in set_list:
    print(j)