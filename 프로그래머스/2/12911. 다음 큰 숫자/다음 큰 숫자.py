def solution(n):
    answer = 0
    bin_n=bin(n)[2:] #이진수로 변환
    count_one = bin_n.count("1")
    bignum=n
    while True:
        bignum+=1 #숫자 하나씩 증가시키기
        bin_bignum=bin(bignum)[2:] #이진수로 변환
        if count_one == bin_bignum.count("1"):
            break
    
    answer=bignum
        
    return answer