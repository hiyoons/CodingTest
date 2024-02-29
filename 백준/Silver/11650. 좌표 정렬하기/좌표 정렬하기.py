import sys

n = int(sys.stdin.readline())
list = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    list.append([a, b])
list.sort()
for j in list:
    print(j[0], j[1])
