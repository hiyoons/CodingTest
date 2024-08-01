first,addUse=map(int,input().split())
n=int(input()) #처리할 고객수

for _ in range(n):
    customer=int(input()) #입력받은 소비량
    if customer < 1000 :
        print(customer,customer*first)
       
    else:
        # 1000 => 1000*first
        add_charge=(customer-1000)*addUse
        print(customer,1000*first+add_charge)
        