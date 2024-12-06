from math import prod
def solution(num_list):
    answer = 0
    res_1=prod(num_list)
    res_2=sum(num_list)**2
    if res_1<res_2:
        return 1
    else:
        return 0
    