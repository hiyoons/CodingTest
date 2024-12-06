def solution(arr, queries):
    for i in range(len(queries)):
        x=queries[i][0]
        y=queries[i][1]
        arr[x],arr[y]=arr[y],arr[x]
    return arr