sound=list(map(int,input().split()))
res=""
for i in range(1,8):
    if sound[i]==sound[i-1]-1:
          res="descending"
    elif sound[i]==sound[i-1]+1:
           res="ascending"
    else :
        res="mixed"
        break
print(res)