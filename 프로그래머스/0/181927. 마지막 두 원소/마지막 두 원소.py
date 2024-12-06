def solution(num_list):
    answer = num_list
    last=len(num_list)
    if num_list[last-1]>num_list[last-2]:
        answer.append(num_list[last-1]-num_list[last-2])
    else:
        answer.append(num_list[last-1]*2)
    return answer