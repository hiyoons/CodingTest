import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    li.append([a, b])
li.sort(key=lambda x: (x[1], x[0]))
for j in li:
    print(j[0], j[1])
