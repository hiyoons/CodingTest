
max=0
sum_train=0

for i in range(10):
    out_train,in_train=map(int,input().split())
    sum_train=sum_train+in_train-out_train
    
    if sum_train > max : 
        max=sum_train

print(max)