def solution(phone_number):
    n=len(phone_number)
    phone_number = phone_number.replace(phone_number[:-4],'*'*(n-4))
    
    return phone_number