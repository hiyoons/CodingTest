import math

def is_prime_number(p):
    for k in range(2, int(math.sqrt(p)) + 1):
        if p%k==0:
            return False
    return True

def solution(n):
    answer=0
    for num in range(2,n+1):
        if is_prime_number(num)==True:
            answer+=1
    
    return answer