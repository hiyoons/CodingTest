list_1 = list(map(int, input().split()))
list2 = [list_1[0], list_1[1], list_1[2] - list_1[0], list_1[3] - list_1[1]]
print(min(list2))