def solution(my_string, index_list):
    answer = ''
    for i in range(len(index_list)):
        index=index_list[i]
        answer+=my_string[index]
    return answer